# Pypeform: Python Package for Typeform Response Piping

Pypeform is a Python package designed to make inbound Typeform responses easier to work with. Provide data as a [Flask request](#flask-requests) or [JSON-based dictionary](#json-data), and access the response in a Pythonic/OOP manner.

__Note:__ not all field types have been implemented, but most basic fields are supported. Feel free to contribute with a PR.

# Installation
Install Pypeform from PyPi:
```
pip install pypeform
```

# Usage
There's a few handy ways to use Pypeform, depending on how you're receiving the webhook data. Most of the time, you'll be dealing with an `Event` object -- a form submission. However, you can also use the `FormResponse` object directly it's JSON constructors if you don't need the `event_id` etc.

## Flask requests
This option is useful if you're handling Typeform data in a Flask web application. This is often the case when you're using a Google Cloud Function, for example.

With a full requests object, you also have the option to verify the response is legitimate, using a pre-shared secret provided in the Typeform webhook dialog. 

```python
from pypeform import Event

request = ... # Flask request object
my_event = Event.from_request(request=request)
form_response = my_event.form_response

for answer in form_response.answers:
    print(answer)

for field in form_response.fields:
    print(field)

for variable in form_response.variables:
    print(variable)
```


## JSON Data
If you have the JSON data of the response in hand, you can still construct an `Event` object:
```python
import json
from pypeform import Event

my_json_data = json.loads(...)

# event_json must be a dict, as provided by the Typeform webhook
Event.from_event_json(event_json=my_json_data)
```

In future versions, we'll add the ability to verify the response using the pre-shared secret (although you'll have to extract the `typeform-signature` header from the webhook headers yourself).