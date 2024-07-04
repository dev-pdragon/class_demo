import requests
import json

URI = "http://api.open-notify.org/iss-now.json"

resp = requests.get(URI)
if resp.status_code == 200:
    json_data = json.dumps(resp.json(), indent=4)
    print(json_data)
print(resp.status_code)
