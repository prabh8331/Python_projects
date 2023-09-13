Certainly! Here's a step-by-step guide for creating a simple Python application that takes two values as input, concatenates them, and prints the result. We'll also cover how to host this application using Flask and Apache2 on port 222. I'll include folder structure guidance as well.

**Step 1: Install Flask:**

If you haven't already, you'll need to install Flask, a Python web framework. You can do this using pip:

```bash
pip install Flask
```

**Step 2: Create a Folder Structure:**

Create a folder for your project and create the following structure:

```
my_concatenator_app/
    +-- app/
    ¦   +-- __init__.py
    ¦   +-- routes.py
    ¦   +-- templates/
    ¦       +-- index.html
    +-- run.py
    +-- venv/ (Virtual Environment)
```

Here's what each component does:

- `my_concatenator_app`: The main project directory.
- `app`: A package directory for your Flask application.
- `__init__.py`: An empty file that marks the `app` directory as a Python package.
- `routes.py`: Contains the Flask routes and application logic.
- `templates`: A directory for HTML templates.
- `index.html`: An HTML template for the web page.
- `run.py`: A script to run your Flask application.
- `venv`: A virtual environment directory for managing project dependencies.

**Step 3: Create Python Files:**

Inside the `my_concatenator_app/app` directory, create the following Python files:

**`__init__.py`:**

```python
from flask import Flask

app = Flask(__name__)

from app import routes
```

**`routes.py`:**

```python
from app import app
from flask import request, render_template

@app.route("/", methods=["GET", "POST"])
def concatenate():
    result = ""
    if request.method == "POST":
        value1 = request.form["value1"]
        value2 = request.form["value2"]
        result = value1 + value2
    return render_template("index.html", result=result)
```

**Step 4: Create HTML Template:**

Inside the `my_concatenator_app/app/templates` directory, create the following HTML template (`index.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Concatenator</title>
</head>
<body>
    <h1>Concatenator</h1>
    <form method="POST">
        <label for="value1">Value 1:</label>
        <input type="text" id="value1" name="value1" required>
        <br>
        <label for="value2">Value 2:</label>
        <input type="text" id="value2" name="value2" required>
        <br>
        <input type="submit" value="Concatenate">
    </form>
    <p>Result: {{ result }}</p>
</body>
</html>
```

**Step 5: Create a Virtual Environment:**

In your project directory (`my_concatenator_app`), create and activate a virtual environment to manage dependencies:

```bash
cd my_concatenator_app
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**Step 6: Install Flask:**

Within the virtual environment, install Flask:

```bash
pip install Flask
```

**Step 7: Run the Flask Application:**

In your project directory, create a Python script (`run.py`) to run the Flask application:

**`run.py`:**

```python
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=222)
```

**Step 8: Configure Apache2 to Listen on Port 222:**

Edit the Apache2 configuration file to make it listen on port 222:

```bash
sudo nano /etc/apache2/ports.conf
```

Add a `Listen` directive:

```apache
Listen 222
```

**Step 9: Create an Apache2 Virtual Host:**

Create a virtual host configuration file for your Python application. Use the following command to create a new configuration file (replace `yourapp` with your project name):

```bash
sudo nano /etc/apache2/sites-available/yourapp.conf
```

Add a basic virtual host configuration:

```apache
<VirtualHost *:222>
    ServerAdmin webmaster@example.com
    ServerName yourserverip
    DocumentRoot /path/to/my_concatenator_app

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Replace `yourserverip` with your server's IP address, and `/path/to/my_concatenator_app` with the actual path to your project directory.

**Step 10: Enable the Virtual Host and Restart Apache2:**

Enable the virtual host and restart Apache2:

```bash
sudo a2ensite yourapp.conf
sudo systemctl restart apache2
```

**Step 11: Access Your Application:**

Access your Python application by navigating to your server's IP address followed by port 222 in a web browser (e.g., `http://yourserverip:222`). You can input two values, click "Concatenate," and see the result.

Your Python application is now hosted on Apache2, running on port 222.





Instead of using port 222, you can choose a higher port number that doesn't require elevated privileges, such as 8080 or 5000






sudo tail -n 10 /var/log/apache2/error.log


[Wed Sep 06 19:43:54.403635 2023] [mpm_event:notice] [pid 8460:tid 140609685305216] AH00492: caught SIGWINCH, shutting down gracefully
[Wed Sep 06 19:43:54.568739 2023] [mpm_event:notice] [pid 8570:tid 139704152094592] AH00489: Apache/2.4.52 (Ubuntu) mod_wsgi/4.9.0 Python/3.10 configured -- resuming normal operations
[Wed Sep 06 19:43:54.568896 2023] [core:notice] [pid 8570:tid 139704152094592] AH00094: Command line: '/usr/sbin/apache2'
[Wed Sep 06 19:44:03.844613 2023] [core:error] [pid 8573:tid 139704129979968] (13)Permission denied: [client 192.168.1.10:56539] AH00035: access to / denied (filesystem path '/home/userver/Python_projects') because search permissions are missing on a component of the path
[Wed Sep 06 19:44:03.884774 2023] [core:error] [pid 8573:tid 139704121587264] (13)Permission denied: [client 192.168.1.10:56539] AH00035: access to /favicon.ico denied (filesystem path '/home/userver/Python_projects') because search permissions are missing on a component of the path, referer: http://192.168.1.111:8088/

check the syntax of your Apache configuration files, including your virtual host configuration:
sudo apache2ctl configtest

sudo systemctl restart apache2

required Apache modules for running a Python Flask application with WSGI 
sudo a2enmod wsgi
sudo a2enmod proxy
sudo a2enmod proxy_http


Apache is indeed running as the www-data user
ps aux | grep apache


ls -l /home/userver/Python_projects/First_python_simple_application_host/app/templates
ls -l /home/userver/Python_projects/First_python_simple_application_host/app
ls -l /home/userver/Python_projects/First_python_simple_application_host
ls -l /home/userver/Python_projects
ls -l /home/userver/venv
ls -l /home/userver
ls -l /home

sudo chmod -R 755 /home/userver/Python_projects/First_python_simple_application_host


sudo chown -R www-data:www-data /home/userver/Python_projects/First_python_simple_application_host


sudo chmod +x /home/userver
sudo chmod +x /home/userver/Python_projects
sudo chmod +x /home/userver/Python_projects/First_python_simple_application_host

sudo chmod +r /home/userver
sudo chmod +r /home/userver/Python_projects
sudo chmod +r /home/userver/Python_projects/First_python_simple_application_host




sudo chmod +x /home/userver/Python_projects
sudo chmod +x /home/userver/Python_projects/First_python_simple_application_host
sudo chmod +x /home/userver/Python_projects/First_python_simple_application_host/app
sudo chmod +x /home/userver/Python_projects/First_python_simple_application_host/app/templates


chmod -R o+rx /home/userver/Python_projects/First_python_simple_application_host/app/templates






Internal Server Error
The server encountered an internal error or misconfiguration and was unable to complete your request.

Please contact the server administrator at [no address given] to inform them of the time this error occurred, and the actions you performed just before this error.

More information about this error may be available in the server error log.

Apache/2.4.52 (Ubuntu) Server at 192.168.1.111 Port 8088


sudo tail -n 20 /var/log/apache2/error.log



[Wed Sep 06 19:45:41.117526 2023] [wsgi:error] [pid 8673:tid 140696671012416] [remote 192.168.1.10:56547]     from app import app as application
[Wed Sep 06 19:45:41.117547 2023] [wsgi:error] [pid 8673:tid 140696671012416] [remote 192.168.1.10:56547]   File "/home/userver/Python_projects/First_python_simple_application_host/app/__init__.py", line 1, in <module>
[Wed Sep 06 19:45:41.117564 2023] [wsgi:error] [pid 8673:tid 140696671012416] [remote 192.168.1.10:56547]     from flask import Flask
[Wed Sep 06 19:45:41.117611 2023] [wsgi:error] [pid 8673:tid 140696671012416] [remote 192.168.1.10:56547] ModuleNotFoundError: No module named 'flask'




cd ~


virtualenv venv


source venv/bin/activate


source ~/venv/bin/activate

cd ~/Python_projects/First_python_simple_application_host

pip install flask

python run.py

deactivate




#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/userver/Python_projects/First_python_simple_application_host')
activate_this = '/home/userver/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from app import app as application



sudo usermod -a -G userver www-data

sudo systemctl restart apache2








to close any website 
sudo a2dissite my_flask_app

sudo systemctl start apache2


at one time only one application could use one virtual env 
