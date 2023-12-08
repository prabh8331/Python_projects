from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Replace with the actual path to your JSON file
# json_file_path = 'C:/Users/prabh/OneDrive/Desktop/Python_projects/python_applications_dev_server/API app test for json/www_app_setup/data.json'
json_file_path = '/var/www/password_api/data.json'

# Read JSON data
def read_json():
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data

# Write JSON data
def write_json(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)

# API endpoint to get JSON data
@app.route('/api/get_data', methods=['GET'])
def get_data():
    data = read_json()
    return jsonify(data)

# API endpoint to update JSON data
@app.route('/api/update_data', methods=['POST'])
def update_data():
    new_data = request.json
    current_data = read_json()
    current_data.update(new_data)
    write_json(current_data)
    return jsonify({'message': 'Data updated successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8023)
