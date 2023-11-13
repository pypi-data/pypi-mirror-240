from typing import Callable, Any
from .exceptions import InvalidEventException

_bus_subscribers: dict[str, list[dict]] = {}

class EventBus():
    @staticmethod
    def on(event: str, /, *, priority: int = 1) -> Callable:
        """Decorator to subscribe a method to an event.

        Args:
            event (str): The event that the method will be subscribed to.
            priority (int, optional): Priority of the callback. Higher values indicate higher priority. Defaults to 1.
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return
        def decorator(callback: Callable) -> Callable:
            EventBus.subscribe(event, callback, priority = priority)
            return callback
        return decorator
    
    @staticmethod
    def subscribe(event: str, callback: Callable, /, *, priority: int = 1) -> None:
        """Subscribes a method to an event.

        Args:
            event (str): The event that the method will be subscribed to.
            callback (Callable): The method that will be subscribed.
            priority (int, optional): Priority of the callback. Higher values indicate higher priority. Defaults to 1.
        """
        if event not in _bus_subscribers:
            _bus_subscribers[event] = []
        _bus_subscribers[event].append({"callback": callback, "priority": priority})
        _bus_subscribers[event].sort(key = lambda subscriber: subscriber["priority"], reverse = True)
    
    @staticmethod
    def unsubscribe(event: str, callback: Callable, /) -> None:
        """Unsubscribes a method from an event.

        Args:
            event (str): The event that the method will be unsubscribed from.
            callback (Callable): The method that will be unsubscribed.
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return
        if event in _bus_subscribers:
            subscribers = _bus_subscribers[event]
            for subscriber in subscribers:
                if subscriber["callback"] == callback:
                    subscribers.remove(subscriber)
                    break

    @staticmethod
    def call(event: str, /, *args, **kwargs) -> None:
        """Calls an event. Use *args and **kwargs to add data to the call.

        Args:
            event (str): The event that will be called.
        """
        result: int | None = EventBus.validate_event(event)
        if result is None:
            return
        if event in _bus_subscribers:
            for subscriber in _bus_subscribers[event]:
                subscriber["callback"](*args, **kwargs)

    @staticmethod
    def validate_event(event: Any) -> int | None:
        """Validates an event.

        Args:
            event (Any): The event type that will be validated.

        Raises:
            InvalidEventException: Raised if the event is not a string.

        Returns:
            int | None: _description_
        """
        if not isinstance(event, str):
            raise InvalidEventException(event)
        return 1
