Step 1: Install Apache

sudo apt update
sudo apt install apache2

sudo systemctl status apache2


change port remove port 80 and replace by any other port
sudo nano /etc/apache2/ports.conf
      Listen 6060




Step 2: Create Website Directory
sudo mkdir -p /var/www/mywebsite 


### display network socket information
ss -nat

cd /etc/apache2

sudo nano ports.conf
add line - Listen 6060



Step 3: Create HTML File
sudo nano /var/www/mywebsite/index.html
Add the following content to the index.html file:

<!DOCTYPE html>
<html>
<head>
    <title>My Simple Website</title>
</head>
<body>
    <h1>Welcome to My Simple Website</h1>
    <p>This is a basic example of a hosted website using Apache.</p>
</body>
</html>




Step 4: Configure Apache
sudo nano /etc/apache2/sites-available/mywebsite.conf
Add the following content to the configuration file, specifying port 6060:

<VirtualHost *:6060>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/mywebsite
    ServerName 192.168.1.111

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>




Step 5: Enable the Virtual Host

sudo a2ensite mywebsite.conf
sudo a2dissite 000-default.conf


Step 6: Restart Apache
sudo systemctl restart apache2


access your website by navigating to http://192.168.1.36:6060


__________end_________________


------------ not used yet ----------------

Install Nginx:
sudo apt update
sudo apt upgrade

sudo apt install nginx
sudo systemctl status nginx
sudo nano /etc/nginx/sites-available/default
listen 80 change to listen 8086
sudo systemctl restart nginx



