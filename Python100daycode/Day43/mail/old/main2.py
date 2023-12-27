
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import pandas as pd
import Python100daycode.Day43.mail.pass_app as pass_app
from email import encoders
import os
import base64


sender_email  = "prabh8331@gmail.com"

sender_password  = pass_app.PassApp().get_data(user=sender_email,app="google_app")

recipient_email = "prabh8221@gmail.com"


message  = MIMEMultipart()
message ['Subject'] = 'HTML-formatted email with image and styling'
message ['From'] = sender_email
message ['To'] = recipient_email




with open('C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/image2.png', 'rb') as file:
    image_data = file.read()
    encoded_image = base64.b64encode(image_data).decode('utf-8')

html_content = ''
with open('C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/index1.html', 'r') as file:
    html_content = file.read().replace('YOUR_BASE64_ENCODED_IMAGE_DATA', encoded_image)

message.attach(MIMEText(html_content, 'html'))



with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

