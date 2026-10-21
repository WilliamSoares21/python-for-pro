import typing_extensions

import requests
import json

api_url = "https://dog.ceo/api/breeds/list/all"

response = requests.get(api_url)

status_code = response.status_code

print("Status code:", status_code)

response_json = response.json()

json_formatado = json.dumps(response_json, indent=4, ensure_ascii=False)
print(json_formatado)
