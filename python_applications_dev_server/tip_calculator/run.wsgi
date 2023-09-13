#!/usr/bin/python3
import sys
sys.path.insert(0, '/var/www/tip_calculator')
activate_this = '/home/virtual_environments/tip_cal_venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from tip_calculator import app as application
