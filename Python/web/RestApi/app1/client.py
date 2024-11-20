import requests
import json

url = 'http://127.0.0.1:5000/get-data'

response = requests.get(url)
js = response.json()
print(js)