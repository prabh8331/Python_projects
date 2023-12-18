import requests
import os

user_name = os.environ.get("mypassappuser")
user_code = os.environ.get("mypassappcode")
timeout = 10
pass_app_url = os.environ.get("mypassappurl")
get_data_url = pass_app_url + "get_data"
response = requests.get(get_data_url, auth=(user_name, user_code), timeout=timeout)
pass_data = response.json()

api_sheety = pass_data["prabh8331@gmail.com"]["sheety_token"]

headers_sheety = {
"Authorization": f"Bearer {api_sheety}"
}

sheety_url = "https://api.sheety.co/69ff39b78b52b370199fe9f25bb1ec09/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    response = requests.get(url=sheety_url,headers=headers_sheety,timeout=timeout)
    excel_data = response.json()
    