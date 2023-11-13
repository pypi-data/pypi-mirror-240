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
```py
python3 -m pip install python-event-bus
```
# Example Usage
### Subscribing to and calling an event
```py
from event_bus import EventBus

@EventBus.on("my_event")
def on_my_event():
    print("Hello, World!")

EventBus.call("my_event")
```
### Output
```
Hello, World!
```
### Unsubscribing from an event
```py
from event_bus import EventBus

@EventBus.on("my_event")
def on_my_event():
    print("Hello, World!")

EventBus.unsubscribe("my_event", on_my_event)
EventBus.call("my_event") # on_my_event will no longer be called because it was unsubscribed from the event
```
### Calling an event with a single positional argument
```py
from event_bus import EventBus

@EventBus.on("my_event")
def on_my_event(data):
    print(f"Received data: {data}")

EventBus.call("my_event", True)
```
### Output
```
Received data: True
```
### Calling an event with *args
```py
from event_bus import EventBus

@EventBus.on("my_event")
def on_my_event(*args):
    print("Event called with the following arguments:")
    for argument in args:
        print(f" - {argument}")

EventBus.call("my_event", 1, 2, 3)
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
from event_bus import EventBus

@EventBus.on("my_event")
def on_my_event(*args, **kwargs):
    print("Event called with the following arguments:")
    for argument in args:
        print(f" - {argument}")

    for kw_argument in kwargs:
        print(f" - {kw_argument} = {kwargs[kw_argument]}")

EventBus.call("my_event", False, value = 10, name = "Bob")
```
### Output
```
Event called with the following arguments:
 - False
 - value = 10
 - name = Bob
```
# Subscribing a method to an event without a decorator
```py
from event_bus import EventBus

def on_my_event():
    print("Hello, World!")

EventBus.subscribe("my_event", on_my_event)
EventBus.call("my_event")
```
### Output
```
Hello, World!
```
# Event callbacks with different priorities
A higher priority indicates a higher priority of callback. The default priority is 1.
```py
from event_bus import EventBus

@EventBus.on("my_event", priority = 0)
def low_priority():
    print("Low priority")

@EventBus.on("my_event", priority = 5)
def high_priority():
    print("High priority")
    
@EventBus.on("my_event")
def default_priority():
    print("Default priority")
    
EventBus.call("my_event")
```
### Output
```
High priority
Default priority
Low priority
```