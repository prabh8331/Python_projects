# Overall comments and Important links

[create ASCII art link](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)


[Random Module Documentation](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)

 
 [python Data structure and list documentation](https://docs.python.org/3/tutorial/datastructures.html)


[cotorhunt](https://colorhunt.co/)



```bash

If you are working with a headless server (without a graphical environment) and want to use Tkinter, you can set up a virtual display using a tool like Xvfb


sudo apt-get install xvfb

Xvfb :1 -screen 0 1024x768x24 &


export DISPLAY=:1

this will list all the -- Run the following command to list processes related to X server:
ps aux | grep X

coder      35893  0.1  0.6 1046680 51880 pts/5   Sl   12:03   0:00 Xvfb :1 -screen 0 1024x768x24
coder      36252  0.0  0.0   6240   712 pts/5    S+   12:04   0:00 grep X

sudo kill 35893


```



```py
# docker pull selenium/standalone-chrome

# docker run -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace "localhost" with the IP address of your Docker host
driver = webdriver.Remote(command_executor='http://192.168.1.36:4444/wd/hub',
                          desired_capabilities={'browserName': 'chrome'})

# Your code that requires a display (e.g., using tkinter or turtle)

driver.quit()




from selenium import webdriver

chrome_capabilities = {
    "browserName": "chrome",
    "browserVersion": "119.0",
    "platformName": "Linux",
    "goog:chromeOptions": {"binary": "/usr/bin/google-chrome"}
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('w3c', False)  # Required for compatibility
chrome_options.update_capabilities(chrome_capabilities)

driver = webdriver.Remote(
    command_executor='http://192.168.1.36:4444/wd/hub',
    options=chrome_options
)




from selenium import webdriver

chrome_capabilities = {
    "browserName": "chrome",
    "browserVersion": "119.0",
    "platformName": "Linux",
    "goog:chromeOptions": {"binary": "/usr/bin/google-chrome"}
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("w3c", False)  # Required for compatibility
chrome_options.add_experimental_option("capabilities", chrome_capabilities)

driver = webdriver.Remote(
    command_executor='http://192.168.1.36:4444/wd/hub',
    options=chrome_options
)


```