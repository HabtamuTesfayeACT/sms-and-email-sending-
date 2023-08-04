import requests

apiSecret = "api key"
phone_number = "phone number"
message = "Hello, this is a test message."
device = "device id"
sim = "1"
priority = 1  

url = "https://hahu.io/api/send/sms"

message = {
    "secret": apiSecret,
    "mode": "devices",
    "device": device,
    "sim": sim,
    "priority": priority,
    "phone": phone_number,
    "message": message
}

try:
    response = requests.post(url, params = message)
    response.raise_for_status()
    print("SMS sent successfully!")
except requests.exceptions.HTTPError as err:
    print(f"An error occurred: {err}")

