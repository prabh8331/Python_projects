import smtplib
import html
from email.mime.text import MIMEText
import requests
import os

my_email = "prabh8331@gmail.com"
user_name = os.environ.get("mypassappuser")
user_code = os.environ.get("mypassappcode")
timeout = 10
pass_app_url = os.environ.get("mypassappurl")
get_data_url = pass_app_url + "get_data"
response = requests.get(get_data_url, auth=(user_name, user_code), timeout=timeout)
pass_data = response.json()
google_app_pass = pass_data[my_email]["google_app"]


mail_body = mail_body1+"\n \n"+mail_body2+"\n \n"+mail_body3+"\n \n"

msg = MIMEText(mail_body, 'plain', 'utf-8')
msg['Subject'] = 'Tesla News Headlines'
msg['From'] = my_email
msg['To'] = my_email


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    
    connection.starttls()
    
    connection.login(user=my_email, password=google_app_pass)
    
    connection.sendmail(from_addr=my_email,
                    to_addrs=[my_email,"prabh8221@gmail.com"],
                    msg=msg.as_string()
                    )


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        
        connection.login(user=my_email, password=password)
        
        connection.sendmail(from_addr=my_email, 
                        to_addrs=[my_email,"prabh8221@gmail.com"], 
                        msg=msg.as_string()
                        )
