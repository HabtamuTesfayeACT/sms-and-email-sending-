import requests

apiSecret = "56236bfbe9417daa75df0a65c1212bc6e10c5dcf"
phone_number = "+251979167656"
message = "Hello, this is a test message."
device = "00000000-0000-0000-c930-8c3ba197866b"
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

