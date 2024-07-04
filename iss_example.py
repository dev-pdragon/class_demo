import requests
import json

URI = "http://apiopen-notify.org/iss-now.json"

resp = requests.get(URI)
if resp.status_code == 200:
    json_data = json.dumps(resp.json(), indent=4)
    print(json_data)

