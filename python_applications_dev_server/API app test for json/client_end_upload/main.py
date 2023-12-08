import requests
import json

# API base URL
# api_base_url = "http://192.168.1.5:8023/api/"
api_base_url = "http://192.168.1.111:8023/api/"
# api_base_url = "http://192.168.1.36:8023/api/"
 
# Endpoint URLs
get_data_url = api_base_url + "get_data"
update_data_url = api_base_url + "update_data"

username = "prabh"
password = "8331"

# Function to get current data
def get_current_data():
    response = requests.get(get_data_url,auth=(username,password))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to update data with a new entry
def update_data(website ,new_entry):
    current_data = get_current_data()
    if current_data is not None:
        # Add a new entry for Myntra
        current_data[website] = new_entry
        
        # Update data using the /api/update_data endpoint
        response = requests.post(update_data_url, json=current_data, auth=(username,password))
        
        if response.status_code == 200:
            print("Data updated successfully.")
        else:
            print(f"Failed to update data. Status code: {response.status_code}")

# Example: New entry for Myntra
website_name = "Google"
new_myntra_entry = {
    "email": "your_myntra_email@example.com",
    "password": "your_myntra_password"
}

# Call the function to update data
update_data(website_name, new_myntra_entry)
