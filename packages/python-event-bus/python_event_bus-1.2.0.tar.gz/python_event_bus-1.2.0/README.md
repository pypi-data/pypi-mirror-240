![PyPiVersion]
![SupportedVersions]
![License]

[PyPiVersion]: https://img.shields.io/pypi/v/python-event-bus
[SupportedVersions]: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-orange
[License]: https://img.shields.io/badge/license-MIT-yellow

# Installation
Built and tested on Python 3.10 and above.<br>
No requirements other than the module itself.
```py
pip install python-event-bus
```
# Example Usage
### Subscribing to and calling an event
```py
from python_event_bus import EventBus

@EventBus.on("example_event")
def on_example_event():
    print("Hello, World!")

EventBus.call("example_event")
```
### Output
```
Hello, World!
```
### Unsubscribing from an event
Unsubscribing from an event will no longer invoke the subscribed method when the event is called.
```py
from python_event_bus import EventBus

@EventBus.on("example_event")
def on_example_event():
    print("Hello, World!")

EventBus.unsubscribe("example_event", on_example_event)
EventBus.call("example_event") # on_example_event will not be called because the subscription is no longer active.
```
### Calling an event with a single positional argument
```py
from python_event_bus import EventBus

@EventBus.on("example_event")
def on_example_event(data):
    print(f"Received data: {data}")

EventBus.call("example_event", True)
```
### Output
```
Received data: True
```
### Calling an event with *args
```py
from python_event_bus import EventBus

@EventBus.on("example_event")
def on_example_event(*args):
    print("Event called with the following arguments:")
    for argument in args:
        print(f" - {argument}")

EventBus.call("example_event", 1, 2, 3)
```
### Output
```
Event called with the following arguments:
 - 1
 - 2
 - 3
```
### Calling an event with **kwargs
```py
from python_event_bus import EventBus

@EventBus.on("example_event")
def on_example_event(*args, **kwargs):
    print("Event called with the following arguments:")
    for argument in args:
        print(f" - {argument}")

    for kw_argument in kwargs:
        print(f" - {kw_argument} = {kwargs[kw_argument]}")

EventBus.call("example_event", False, value = 10, text = "Hello")
```
### Output
```
Event called with the following arguments:
 - False
 - value = 10
 - text = Hello
```
# Subscribing a method to an event without a decorator
```py
from python_event_bus import EventBus

def on_example_event():
    print("Hello, World!")

EventBus.subscribe("example_event", on_example_event) # on_example_event is subscribed to the event "example_event"
EventBus.call("example_event")
```
### Output
```
Hello, World!
```
# Using the event bus throughout different files
`main.py`
```py
from python_event_bus import EventBus
from test import call_example_event

@EventBus.on("example_event")
def on_example_event(data):
    print(f"Example event called with data: {data}")

call_example_event()
```
`test.py`
```py
from python_event_bus import EventBus

def call_example_event():
    EventBus.call("example_event", "Hello from test.py")
```
### Output
```
Example event called with data: Hello from test.py
```
# Event callbacks with different priorities
A higher priority indicates a higher priority of callback. The default priority is 1.
```py
from python_event_bus import EventBus

@EventBus.on("example_event", priority = 0)
def low_priority():
    print("Low priority")

@EventBus.on("example_event", priority = 5)
def high_priority():
    print("High priority")
    
@EventBus.on("example_event")
def default_priority():
    print("Default priority")
    
EventBus.call("example_event")
```
### Output
```
High priority
Default priority
Low priority
```
# Using the event bus context manager
Note that existing methods such as `subscribe`, `unsubscribe`, and `call` will still function correctly inside of a context manager.
```py
from python_event_bus import EventBus, EventBusContextManager

with EventBusContextManager() as event_bus:
    # Use the context manager to create methods
    # that are subscribed to an event only for
    # the lifetime of the context-managed bus.
    @event_bus.on("example_event")
    def on_example_event(data):
        print(f"Example event was called. Data: {data}")
        
    # Use the EventBus class to call events even if they are created within the context manager.
    EventBus.call("example_event", 1)
    
# All methods that are subscribed to events during the lifetime of the context
# manager will be automatically unsubscribed when the context manager exits.
# The subscription on_example_event that was created within the context manager
# is no longer active.
EventBus.call("example_event", 2) # on_example_event will not be called.
```
### Output
```
Example event was called. Data: 1
```