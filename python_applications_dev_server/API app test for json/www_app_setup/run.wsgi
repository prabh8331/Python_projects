#!/usr/bin/python3
import sys
import os

# Adjust the path to point to your application directory
sys.path.insert(0, '/var/www/password_api')

# Activate the virtual environment
activate_this = '/home/virtual_environments/password_api_venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import the main Flask application object from your main script
from main import app as application
