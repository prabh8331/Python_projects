import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import pandas as pd
import Python100daycode.Day43.mail.pass_app as pass_app
from email import encoders
import os



sender_email  = "prabh8331@gmail.com"

sender_password  = pass_app.PassApp().get_data(user=sender_email,app="google_app")

recipient_email = "prabh8221@gmail.com"


message  = MIMEMultipart()
message ['Subject'] = 'HTML-formatted email with image and styling'
message ['From'] = sender_email
message ['To'] = recipient_email


html_content = ''
with open('C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/index.html', 'r') as file:
    html_content = file.read()

message.attach(MIMEText(html_content, 'html'))

with open('C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/image2.png', 'rb') as file:
    img = MIMEImage(file.read(), name=os.path.basename('image2.png'))
    message.attach(img)


with open('C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/style.css', 'r') as file:
    css_content = file.read()
    part = MIMEBase('text', 'css')
    part.set_payload(css_content)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="style.css"')
    message.attach(part)



with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())



