import json
import base64
from cloudevents.http import CloudEvent
from flask import Request

def on_user_create(event_or_request, context=None):
    
    if isinstance(event_or_request, Request):
        data = event_or_request.get_json(silent=True) or {}
    
   
    else:
        event = event_or_request
        raw_data = event.get("data", b"")
        
        
        if isinstance(raw_data, bytes):
            try:
                data_str = raw_data.decode("utf-8").strip()
            except UnicodeDecodeError:
                data_str = raw_data.decode("latin1").strip()
        elif isinstance(raw_data, str):
            data_str = raw_data.strip()
        else:
            data_str = ""

        try:
            data = json.loads(data_str) if data_str else {}
        except json.JSONDecodeError:
            print(f"Invalid JSON received: {data_str}")
            data = {}

    
    value = data.get("value", {})
    name = value.get("name", "Unknown")
    email = value.get("email", "Unknown")
    age = value.get("age", 0)
    role = value.get("role", "Unknown")

    
    print(f"Doc is created: Name={name}, Email={email}, Age={age}, Role={role}")

   
    if isinstance(event_or_request, Request):
        return "Success", 200
    else:
        return None
