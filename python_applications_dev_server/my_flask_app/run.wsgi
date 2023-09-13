#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/userver/Python_projects/First_python_simple_application_host')
activate_this = '/home/userver/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from app import app as application

