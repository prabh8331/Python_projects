import requests
import os

from datetime import datetime
import pytz
timezone_ist = pytz.timezone('Asia/Kolkata')
time_now = datetime.now(timezone_ist) 

today = time_now.strftime("%d/%m/%Y")
time = time_now.strftime("%I:%M:%S %p")
# time = time_now.strftime("%H:%M:%S")


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

sheety_url = "https://api.sheety.co/69ff39b78b52b370199fe9f25bb1ec09/myWorkoutLogs/workouts"

response = requests.get(url=sheety_url,headers=headers_sheety)

excel_data = response.json()


workouts = excel_data['workouts']

id = len(workouts)+2

appid = pass_data["prabh8331@gmail.com"]["nutritionix_appid"]
apikey = pass_data["prabh8331@gmail.com"]["nutritionix_api"]


endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Enter what you did today: ")

# query = "I did 30 mins of running and 30 mins of swimming"

params = {
    "query" : query
}

headers = {
    "x-app-id" : appid,
    "x-app-key" : apikey
}

response = requests.post(url=endpoint, json=params, headers=headers)

data = response.json() 

for wkt in data["exercises"]:
    exercise = wkt["name"]
    duration = wkt["duration_min"]
    calories = wkt["nf_calories"]
    new_entry = {'id': id, 'date': today, 'time': time, 'exercise': exercise, 'duration': duration, 'calories': calories}
    data_post ={'workout': new_entry}
    response = requests.post(url=sheety_url, json=data_post, headers=headers_sheety)
    id+=1

