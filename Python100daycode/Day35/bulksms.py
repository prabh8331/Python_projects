import requests

url = "https://api.bulksms.com/v1/messages"

token_id="46EA330519524FA39584B438E6BA0F48-02-8"

token_secret="GscPy#FEXUw3yCdhRrPP0qrKw*lBO"

basic_auth="Authorization: Basic NDZFQTMzMDUxOTUyNEZBMzk1ODRCNDM4RTZCQTBGNDgtMDItODpHc2NQeSNGRVhVdzN5Q2RoUnJQUDBxckt3KmxCTw=="


headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic NDZFQTMzMDUxOTUyNEZBMzk1ODRCNDM4RTZCQTBGNDgtMDItODpHc2NQeSNGRVhVdzN5Q2RoUnJQUDBxckt3KmxCTw==",
}

data = {
    # "from": "+917042450972",
    "to": "+917042450972",  # Replace with the recipient's phone number
    "body": "Hello World!",

}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
