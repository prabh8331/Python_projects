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


```


```bash
# required Apache modules for running a Python Flask application with WSGI 
sudo apt update
sudo apt install libapache2-mod-wsgi

sudo a2enmod wsgi
sudo a2enmod proxy
sudo a2enmod proxy_http
```










```bash
# Create a new Apache configuration file
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