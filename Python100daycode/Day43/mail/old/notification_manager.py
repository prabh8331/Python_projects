import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import Python100daycode.Day43.mail.pass_app as pass_app

my_email = "prabh8331@gmail.com"

google_app_pass = pass_app.PassApp().get_data(user=my_email,app="google_app")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self, subject, mail_body, data, to):
        
        df = pd.DataFrame(data)

        html_table = df.to_html(index=False)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = my_email
        msg['To'] = my_email

        msg.attach( MIMEText(mail_body, 'plain', 'utf-8'))

        msg.attach(MIMEText(html_table, 'html'))

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            
            connection.login(user=my_email, password=google_app_pass)
            
            connection.sendmail(from_addr=my_email, 
                            to_addrs=to, 
                            msg=msg.as_string()
                            )

