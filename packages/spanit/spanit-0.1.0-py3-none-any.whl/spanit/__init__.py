"""
TSpan, the main entry point to the spanit package.
"""
from __future__ import annotations

import logging
import threading
from collections import defaultdict
from datetime import datetime, timedelta
from functools import wraps
from io import StringIO
from logging import Logger, getLevelName
from types import TracebackType
from typing import Callable, Type, TypeVar, Any, ParamSpec
from uuid import uuid4


def default_create_extra_msg(_label: str, extra: dict) -> str:
    """
    The default extra message implementation.

    :param _label: The label of the :class:`TSpan` instance.
    :param extra: The `extra` of the :class:`TSpan` instance.
    :return: " with: {key=%(key)r}"
    """
    if not extra:
        return ""

    return " with: " + " ".join(f"{{{key}=%({key})r}}" for key in extra)


def default_create_span_id(_label: str, _extra: dict) -> str:
    """
    The default span id implementation.

    :param _label: The label of the :class:`TSpan` instance.
    :param _extra: The `extra` of the :class:`TSpan` instance.
    :return: An 8 character identifier for the :class:`TSpan` instance.
    """
    return uuid4().hex[:8]


T = TypeVar("T")


def identity(obj: T) -> T:
    """
    Returns the given object unchanged.

    :param obj: The object to return.
    :return: The given object.
    """
    return obj


def default_extra_datetime_formatter(dt: datetime) -> str:
    """
    The default extra datetime formatter implementation.

    :param dt: The datetime to format.
    :return: A rfc3339~ string which assumes UTC.
    """
    return f"{dt.strftime('%Y-%m-%dT%H:%M:%S')!s}.{int(dt.microsecond / 1000):03d}Z"


def default_extra_timedelta_formatter(td: timedelta) -> int:
    """
    The default extra timedelta formatter implementation.

    :param td: The timedelta to format.
    :return: Total milliseconds.
    """
    return int(td.total_seconds() * 1000)


DatetimeFormatter = Callable[[datetime], Any]
TimedeltaFormatter = Callable[[timedelta], Any]

_stacks: defaultdict[int, list] = defaultdict(list)


def _get_stack() -> list[TSpan]:
    stack = _stacks[threading.get_ident()]
    return stack


class TSpanException(Exception):
    """
    Base exception for the :mod:`spanit` package.
    """


class AddIdFilter(logging.Filter):
    """
    A filter that adds the spanit ID to the log message.
    """

    def __init__(self, id_key: str, id_value: str, depth: int) -> None:
        super().__init__()
        self.id_key = f"{id_key}_{depth}"
        self.id_value = id_value

    def filter(self, record: logging.LogRecord) -> bool:
        setattr(record, self.id_key, self.id_value)

        if isinstance(record.args, dict):
            record.msg = f"[%({self.id_key})s] {record.msg}"
            record.args[self.id_key] = self.id_value
        elif isinstance(record.args, tuple):
            record.msg = f"[%s] {record.msg}"
            record.args = self.id_value, *record.args

        return super().filter(record)


P = ParamSpec("P")
R = TypeVar("R")


class TSpan:
    def __init__(
        self,
        label: str,
        logger: Logger,
        extra: dict | None = None,
        *,
        disabled: bool = False,
        datetime_now: Callable[[], datetime] = datetime.utcnow,
        field_name_prefix: str = "tspan_",
        apply_prefix_only_to_span_fields: bool = True,
        create_extra_msg: Callable[[str, dict], str] = default_create_extra_msg,
        create_span_id: Callable[[str, dict], str] = default_create_span_id,
        args_datetime_formatter: DatetimeFormatter = identity,
        args_timedelta_formatter: TimedeltaFormatter = identity,
        extra_datetime_formatter: DatetimeFormatter = default_extra_datetime_formatter,
        extra_timedelta_formatter: TimedeltaFormatter = default_extra_timedelta_formatter,
        timing_log_level: str = "DEBUG",
        timing_start_log_msg: str = "Starting %({field_name_prefix}label)r at %({field_name_prefix}start)s",
        timing_end_log_msg: str = "Finished %({field_name_prefix}label)r at %({field_name_prefix}end)s after %({field_name_prefix}duration)s",
        exception_log_level: str = "ERROR",
        exception_log_msg: str = "Error during %({field_name_prefix}label)r",
        include_traceback: bool = True,
    ) -> None:
        self.label = label
        self.logger = logger
        self.extra: dict = extra or {}
        self.disabled = disabled
        self.datetime_now = datetime_now
        self.field_name_prefix = field_name_prefix
        self.args_datetime_formatter = args_datetime_formatter
        self.extra_datetime_formatter = extra_datetime_formatter
        self.args_timedelta_formatter = args_timedelta_formatter
        self.extra_timedelta_formatter = extra_timedelta_formatter
        self.timing_log_level = timing_log_level
        self.exception_log_level = exception_log_level

        self._include_traceback = include_traceback
        self._apply_prefix_only_to_span_fields = apply_prefix_only_to_span_fields

        # Create the extra suffix with jus the original extra, before we add things
        extra_suffix = create_extra_msg(label, self.extra)

        id_key = f"{self.field_name_prefix}id"
        self.id = self.extra.get(id_key, create_span_id(label, self.extra))

        def format_msg(msg: str):
            final_msg = StringIO()
            # final_msg.write(ids_prefix)
            final_msg.write(msg.format(field_name_prefix=self.field_name_prefix))
            final_msg.write(extra_suffix)

            return final_msg.getvalue()

        # Add the suffix and prefix to the messages
        self._timing_start_log_msg = format_msg(timing_start_log_msg)
        self._timing_end_log_msg = format_msg(timing_end_log_msg)
        self._exception_log_msg = format_msg(exception_log_msg)

        self.depth = len(_get_stack())

        self.filter = AddIdFilter(id_key, self.id, self.depth)

        self.start: datetime
        self.end: datetime
        self.duration: timedelta

    def _create_fields(
        self,
        datetime_formatter: DatetimeFormatter,
        timedelta_formatter: TimedeltaFormatter,
    ) -> dict:
        fields = self.extra.copy()

        for attr in ("id", "label", "start", "end", "duration"):
            if (value := getattr(self, attr, None)) is not None:
                # If we only want to add the prefix to these fields,
                # then we will add it here and skip it later.
                # Otherwise, we just add the prefix to everything, including these, later.
                if self._apply_prefix_only_to_span_fields:
                    attr = self.field_name_prefix + attr

                fields[attr] = value

        for key, value in fields.items():
            if not self._apply_prefix_only_to_span_fields:
                key = self.field_name_prefix + key

            if isinstance(value, datetime):
                value = datetime_formatter(value)
            elif isinstance(value, timedelta):
                value = timedelta_formatter(value)

            fields[key] = value

        return fields

    def create_args(self):
        return self._create_fields(
            self.args_datetime_formatter, self.args_timedelta_formatter
        )

    def create_extra(self):
        return self._create_fields(
            self.extra_datetime_formatter, self.extra_timedelta_formatter
        )

    def __call__(self, function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            with self:
                return function(*args, **kwargs)

        return inner

    def __enter__(self):
        self.start = self.datetime_now()

        if self.disabled:
            return self

        stack = _get_stack()
        stack.append(self)

        if self._apply_prefix_only_to_span_fields:
            self.logger.filters.insert(
                len(self.logger.filters) - len(stack) + 1, self.filter
            )

        self.logger.log(
            getLevelName(self.timing_log_level),
            self._timing_start_log_msg,
            self.create_args(),
            extra=self.create_extra(),
            stacklevel=2,
        )

        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ):
        self.end = self.datetime_now()
        self.duration = self.end - self.start

        if self.disabled:
            return

        _get_stack().pop()

        args = self.create_args()
        extra = self.create_extra()

        if exc_type is not None:
            self.logger.log(
                getLevelName(self.exception_log_level),
                self._exception_log_msg,
                args,
                extra=extra,
                exc_info=(exc_type, exc_value, traceback)
                if self._include_traceback
                else False,
                stacklevel=2,
            )

        self.logger.log(
            getLevelName(self.timing_log_level),
            self._timing_end_log_msg,
            args,
            extra=extra,
            stacklevel=2,
        )

        self.logger.removeFilter(self.filter)
