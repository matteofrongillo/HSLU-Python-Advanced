import requests
import json
response = requests.get("https://en.wikipedia.org/w/api.php", params={
    "action": "query",
    "list": "search",
    "srsearch": "HSLU",
    "format": "json"
})
print(response)
print(response.url)
json_str = response.json()
print(json.dumps(json_str, indent=2, sort_keys=True))