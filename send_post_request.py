import requests
# Send POST request to /record endpoint with JSON payload
response = requests.post("http://0.0.0.0:8000/record", json={"engine_temperature": 0.3})
