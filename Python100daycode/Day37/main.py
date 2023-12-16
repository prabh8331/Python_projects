import requests
import os

user_name = os.environ.get("mypassappuser")
user_code = os.environ.get("mypassappcode")
timeout = 10
pass_app_url = os.environ.get("mypassappurl")
get_data_url = pass_app_url + "get_data"
response = requests.get(get_data_url, auth=(user_name, user_code), timeout=timeout)
pass_data = response.json()

pixela_endpoint = "https://pixe.la/v1/users"
username = "prabh"
token = pass_data["prabh8331@gmail.com"]["pixela"]
# print(token)


user_params = {
    "token" : token,
    "username" : username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id" : "gph1",
    "name" : "Sleep Cycle Track",
    "color" : "shibafu",
    "unit" : "OnTime",
    "type" : "int",
    "timezone" : "Asia/Kolkata"
}

#x-
headers = {
    "X-USER-TOKEN" : token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# print(response.text)

## view the graph --> "https://pixe.la/v1/users/prabh/graphs/gph1.html"


from datetime import datetime, timedelta
import pytz
timezone_ist = pytz.timezone('Asia/Kolkata')
time_now = datetime.now(timezone_ist) 
today = time_now.date() + timedelta(days=-4)
today = today.strftime("%Y%m%d")
# today = today.replace("-","")

pixel_post_endpoint = f"{pixela_endpoint}/{username}/graphs/gph1"

pixel_post_params = {
    "date" : today,
    "quantity" : "3"
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)

# print(response.text)


### Use Put method to update value

date=datetime(year=2023 , month=12, day= 16).strftime("%Y%m%d")

pixel_put_endpoint = f"{pixela_endpoint}/{username}/graphs/gph1/{date}"

pixel_put_params = {
    "quantity" : "2"
}

# response = requests.put(url=pixel_put_endpoint, json=pixel_put_params, headers=headers)

response = requests.delete(url=pixel_put_endpoint, headers=headers)

print(response.text)
