### Steps for tip_calculator 

#### once developlment server is giving results then move the folder to production : - 
cd /home/userver/Python_projects/python_applications_dev_server

sudo cp -r tip_calculator /var/www/tip_calculator

cd /home/userver/Python_projects/python_applications_dev_server/Apache2_conf_for_python_apps

sudo cp tip_calculator.conf /etc/apache2/sites-available/tip_calculator.conf


#### setup virtual env
# sudo chown -R userver:userver /home/virtual_environments      --not needed if userver has assess already 

cd /home/virtual_environments

virtualenv tip_cal_venv

source /home/virtual_environments/tip_cal_venv/bin/activate

cd /var/www/tip_calculator/

pip install flask

python run.py

deactivate


sudo nano /etc/apache2/ports.conf
add line --> 
Listen 8891

For virtual host setup tip_calculator
sudo a2ensite tip_calculator
sudo systemctl restart apache2
