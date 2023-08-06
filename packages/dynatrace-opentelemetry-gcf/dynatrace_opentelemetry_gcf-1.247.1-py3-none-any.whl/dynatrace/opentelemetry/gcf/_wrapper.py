import functools
from typing import Any, Callable, TypeVar, cast

from dynatrace.opentelemetry.gcf._trigger import determine_trigger

HandlerT = TypeVar("HandlerT", bound=Callable[..., Any])


def wrap_handler(
    handler: HandlerT = None, flush_on_exit: bool = True
) -> HandlerT:
    """A decorator for tracing Google Cloud Function invocations.

    The decorator wraps the given function handler and creates a span for every
    invocation.

    Example usage::

        @wrap_handler
        def handler(req: flask.Request) -> flask.Response:
            # do something
            return flask.Response("Hello World, 200)

    Args:
        handler: the Google Cloud Function handler to wrap.
        flush_on_exit: determines whether to flush spans on exit or not.
    """
    if handler is None:
        return functools.partial(wrap_handler, flush_on_exit=flush_on_exit)

    if not callable(handler):
        raise ValueError(
            f"'handler': expected callable but got '{type(handler)}'"
        )

    @functools.wraps(handler)
    def _wrapper(*args, **kwargs):
        trigger = determine_trigger(args, kwargs)
        with trigger.start_as_current_span(flush_on_exit) as span:
            result = handler(*args, **kwargs)
            trigger.set_exit_attributes(span, result)
        return result

    return cast(HandlerT, _wrapper)
