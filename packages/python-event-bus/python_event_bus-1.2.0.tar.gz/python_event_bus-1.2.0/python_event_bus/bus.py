from typing import Callable, Any
from .exceptions import InvalidEventException

_bus_subscribers: dict[str, list[dict]] = {}

class EventBus():
    @staticmethod
    def on(event: str, /, *, priority: int = 1) -> Callable | int:
        """Decorator to subscribe a method to an event.

        Args:
            event (str): The event that the method will be subscribed to.
            priority (int, optional): Priority of the callback. Higher values indicate higher priority. Defaults to 1.

        Example:
            >>> @EventBus.on("example_event")
            ... def on_example_event(*args, **kwargs):
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return 0
        def wrapper(callback: Callable) -> Callable:
            EventBus.subscribe(event, callback, priority = priority)
            return callback
        return wrapper
    
    @staticmethod
    def subscribe(event: str, callback: Callable, /, *, priority: int = 1) -> int | None:
        """Subscribes a method to an event.

        Args:
            event (str): The event that the method will be subscribed to.
            callback (Callable): The method that will be subscribed.
            priority (int, optional): Priority of the callback. Higher values indicate higher priority. Defaults to 1.

        Example:
            >>> def on_example_event():
            ...     print("Example event called")
            >>>
            >>> EventBus.subscribe("example_event", on_example_event)
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return 0
        
        if event not in _bus_subscribers:
            _bus_subscribers[event] = []
        _bus_subscribers[event].append({"callback": callback, "priority": priority})
        _bus_subscribers[event].sort(key = lambda subscriber: subscriber["priority"], reverse = True)
    
    @staticmethod
    def unsubscribe(event: str, callback: Callable, /) -> int | None:
        """Unsubscribes a method from an event.

        Args:
            event (str): The event that the method will be unsubscribed from.
            callback (Callable): The method that will be unsubscribed.

        Example:
            >>> @EventBus.on("example_event")
            ... def on_example_event():
            ...     print("Example event called")
            >>>
            >>> EventBus.unsubscribe("example_event", on_example_event)
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return 0
        
        if event in _bus_subscribers:
            subscribers = _bus_subscribers[event]
            for subscriber in subscribers:
                if subscriber["callback"] == callback:
                    subscribers.remove(subscriber)
                    break

    @staticmethod
    def call(event: str, /, *args, **kwargs) -> int:
        """Calls an event with optional data, invoking subscribed callbacks.

        Args:
            event (str): The event to be called.
            *args: Additional positional arguments to be passed to the callbacks.
            **kwargs: Additional keyword arguments to be passed to the callbacks.

        Returns:
            int: The number of event subscribers that were successfully called.
        
        Example:
            >>> count: int = EventBus.call("example_event")
            >>> print(f"{count} subscriber(s) were called for the event 'example_event'")
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return 0
        
        call_count: int = 0

        if event in _bus_subscribers:
            for subscriber in _bus_subscribers[event]:
                subscriber["callback"](*args, **kwargs)
                call_count += 1

        return call_count

    @staticmethod
    def validate_event(event: Any, /) -> int | None:
        """Validates an event.

        Args:
            event (Any): The event type that will be validated.

        Raises:
            InvalidEventException: Raised if the event is not a string.

        Returns:
            int | None: Will return 1 if the event is valid.
        """
        if not isinstance(event, str):
            raise InvalidEventException(event)
        return 1

class EventBusContextManager():
    """A context-managed event bus. All methods that are subscribed in the
    lifetime of the bus will be unsubscribed when the context manager exits."""
    def __init__(self) -> None:
        self.__bus_subscribers: dict[str, list[dict]] = {}

    def on(self, event: str, /, *, priority: int = 1) -> Callable | int:
        """Decorator to subscribe a method to an event.

        Args:
            event (str): The event that the method will be subscribed to.
            priority (int, optional): Priority of the callback. Higher values indicate higher priority. Defaults to 1.

        Example:
            >>> with EventBusContextManager() as event_bus:
            ...     @event_bus.on("example_event")
            ...     def on_example_event(*args, **kwargs):
        """
        def wrapper(callback: Callable) -> Callable:
            EventBus.subscribe(event, callback, priority = priority)
            if event not in self.__bus_subscribers:
                self.__bus_subscribers[event] = []
            self.__bus_subscribers[event].append({"callback": callback, "priority": priority})
            self.__bus_subscribers[event].sort(key = lambda subscriber: subscriber["priority"], reverse = True)
            return callback
        return wrapper
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        for event in self.__bus_subscribers:
            for subscriber in self.__bus_subscribers[event]:
                EventBus.unsubscribe(event, subscriber["callback"])