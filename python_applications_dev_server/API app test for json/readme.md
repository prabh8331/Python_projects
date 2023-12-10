# API create

## Install Apache2
```bash
# Update package list
sudo apt update

# Install Apache2
sudo apt install apache2

# Start Apache2
sudo systemctl start apache2

# Enable Apache2 to start on boot
sudo systemctl enable apache2

# Open port 8023 in the firewall

sudo ufw allow 8023
```


## PassWord Protect a Directory

```bash
# Install Apache utilities
sudo apt install apache2-utils

# Create a password file
sudo htpasswd -c /etc/apache2/.htpasswd prabh
# You will be prompted to enter and confirm a password for the username.

#modify passowrd
sudo htpasswd -m /etc/apache2/.htpasswd prabh


```


```bash
#Open Port 
sudo nano /etc/apache2/ports.conf

    Listen 8023 
```


```bash
##python related packeges and library install
sudo apt install python3-pip
pip install flask

sudo apt install python3-virtualenv  #to create virtule env

## give premission to /home/virtual_environments
ls -ld /home/virtual_environments
sudo chown prabh:prabh /home/virtual_environments
sudo chmod 775 /home/virtual_environments


```


```bash
# required Apache modules for running a Python Flask application with WSGI 
sudo apt update
# sudo apt install libapache2-mod-wsgi

sudo apt install libapache2-mod-wsgi-py3

sudo a2enmod wsgi
# sudo a2enmod proxy
# sudo a2enmod proxy_http
```


```bash

cd /var/www/

sudo mkdir password_api

cd password_api/

sudo nano data.json

```
`data.json`
```json
{
  "Amazon": {
    "email": "prabh8331@gmail.com",
    "password": "ylXN0)xgOM#1o"
  },
  "Myntra": {
    "email": "your_myntra_email@example.com",
    "password": "your_myntra_password"
  },
  "Google": {
    "email": "your_myntra_email@example.com",
    "password": "your_myntra_password"
  }
}

```

```bash

sudo nano main.py

### paste the www_app_setup main.py
```





virtual env setup
```bash
cd /home/virtual_environments

virtualenv password_api_venv

source /home/virtual_environments/password_api_venv/bin/activate

cd /var/www/password_api/

pip install flask

python main.py

deactivate

```



```bash
sudo nano run.wsgi

```

```py

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

```


```bash
# Create a new Apache configuration file
cd /etc/apache2/sites-available
sudo nano /etc/apache2/sites-available/password_api.conf

```

`password_api.conf:`
```html

<VirtualHost *:8080>
    ServerAdmin webmaster@example.com
    DocumentRoot /path/to/your/api

    <Directory "/path/to/your/api">
        AuthType Basic
        AuthName "Restricted Access"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user

        WSGIDaemonProcess your-app-name threads=5
        WSGIScriptAlias / /path/to/your/api/your-api-script.wsgi

        <IfVersion < 2.4>
            WSGIProcessGroup your-app-name
        </IfVersion>

        <IfVersion >= 2.4>
            WSGIApplicationGroup %{GLOBAL}
        </IfVersion>
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```


```conf
<VirtualHost *:8023>
    ServerName 192.168.1.111

    Options -Indexes

    WSGIDaemonProcess password_api threads=5
    WSGIScriptAlias / /var/www/password_api/run.wsgi

    <Directory /var/www/password_api>
        WSGIProcessGroup password_api
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


```

```conf

<VirtualHost *:8023>
    ServerName 192.168.1.111

    Options -Indexes

    WSGIDaemonProcess password_api threads=5
    WSGIScriptAlias / /var/www/password_api/run.wsgi

    <Directory /var/www/password_api>
        WSGIProcessGroup password_api
        WSGIApplicationGroup %{GLOBAL}
        
        AuthType Basic
        AuthName "Restricted Access"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


```


```bash
# run this and host the password_api 
sudo a2ensite password_api.conf
sudo systemctl reload apache2

```



```bash
sudo tail -f /var/log/apache2/error.log

```

```bash
##check the premissions
ls -l /var/www/password_api/data.json
#-rw-r--r-- 1 www-data www-data 12345 Dec 8 16:00 /var/www/password_api/data.json


#change the premissinos 
sudo chown www-data:www-data /var/www/password_api/data.json
sudo chmod 644 /var/www/password_api/data.json



```




```bash
# making git repository of data.json in home dictory
# paste the data file and change the running premmsion also change the main.py code
sudo chown www-data:www-data /home/mypassdata/prabh_pass_data.json
sudo chmod 644 /home/mypassdata/prabh_pass_data.json


sudo nano update.txt
# sudo chown www-data:www-data /home/mypassdata/update.txt
# sudo chmod 644 /home/mypassdata/update.txt

sudo chown prabh:www-data /home/mypassdata/update.txt
sudo chmod ug+rwx /home/mypassdata/update.txt




#install at function to commit changes every hour
sudo apt install at
at -V

create a bash file to add an commit

sudo nano autocommit.bash
```

`autocommit.bash`
```bash
git add prabh_pass_data.json                                                      

git commit -m "password update/addition"

echo "bash /home/mypassdata/autocommit.bash" | at now + 1 hour
```

atq

date

atrm 7

echo "bash /home/mypassdata/autocommit.bash" | at now + 1 minute




```bash
######look git log and go to the older version of the file

git log --oneline -n 5

git show 2666b37:prabh_pass_data.json

git show f426abc:prabh_pass_data.json

git checkout f426abc

git checkout master

```