import functions_framework
import base64
import json

@functions_framework.cloud_event
def on_file_upload(cloud_event):
    msg = cloud_event.data["message"]
    data = base64.b64decode(msg["data"]).decode("utf-8")

    print("RAW MESSAGE:", data)
    try:
        payload = json.loads(data)
        print("Event:", payload.get("event"))
        print("User:", payload.get("user"))
        print("Age:", payload.get("age"))
        print("Role:", payload.get("role"))
    except json.JSONDecodeError as e:
        print("JSON parse error:", e)
