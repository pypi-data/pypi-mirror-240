import logging
import sys
from pprint import pprint

from tspan import TSpan


class DebugHandler(logging.StreamHandler):
    def handle(self, record: logging.LogRecord) -> bool:
        self.stream.write(repr(record.msg) + " % " + str(record.args) + "\n")
        self.stream.write(str(record.__dict__) + "\n")

        result = super().handle(record)

        self.stream.write("\n")
        return result


log = logging.getLogger(__name__)
fmt = logging.Formatter()
handler = DebugHandler(sys.stderr)
handler.setFormatter(fmt)
log.addHandler(handler)
log.setLevel("DEBUG")


@TSpan("Foo", log)
def foo():
    return 5


foo()

with TSpan("0", log, {"a": 1}) as a:
    log.debug("Message: %r", "value")
    log.debug("Message: %(key)r", {"key": "value"})
    with TSpan("1", log, {"b": 2}) as b:
        log.debug("Message: %r", "value")
        log.debug("Message: %(key)r", {"key": "value"})
        with TSpan("2", log, {"c": 3}) as c:
            log.debug("Message: %r", "value")
            log.debug("Message: %(key)r", {"key": "value"})

pprint(a)
pprint(b)
pprint(c)
