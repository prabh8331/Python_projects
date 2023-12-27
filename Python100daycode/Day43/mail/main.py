import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import pandas as pd
import pass_app
from email import encoders
import os
import base64

# Email Configuration
smtp_server = 'smtp.gmail.com' # Outlook SMTP server
port = 587 # Outlook SMTP port
sender_email = 'prabh8331@gmail.com'
sender_password = pass_app.PassApp().get_data(user=sender_email,app="google_app")
recipients = 'prabh8221@gmail.com'

message = MIMEMultipart()
message['Subject'] = 'HTML-formatted email with image and styling'
message['From'] = sender_email
message['To'] = recipients


# Assuming `image_path` is the path to your image file
image_path = 'C:/Users/prabh/OneDrive/Desktop/Python_projects/Python100daycode/Day43/mail/image2.png'
image_cid = 'image_cid'

with open(image_path, 'rb') as file:
    image_data = file.read()



# Encode the image data in base64


encoded_image = base64.b64encode(image_data).decode('utf-8')

# Create a MIME image part
image_part = MIMEImage(image_data, name=os.path.basename(image_path))
image_part.add_header('Content-ID', f'<{image_cid}>')
image_part.add_header('Content-Disposition', 'inline')
image_part.add_header('Content-Type', 'image/png')

# Attach the image part to your MIMEMultipart message
message.attach(image_part)


html_content = f"""
<html>

<body>
    <table border="0" cellspacing="0" cellpadding="0" width="650px">
        <tr>
            <td style="border-width: 1px; border-style: solid; border-color: gray; border-radius: 0px; padding: 4px;">

                <table border="0" cellspacing="0" cellpadding="0" width="100%">
                    <tr>
                        <td
                            style="border-width: 2px; border-style: solid; border-color: black; border-radius: 0px; padding: 2px; background-color: #31006f;">
                            <table border="0" cellspacing="0" cellpadding="0" width="100%">
                                <tr>
                                    <td style="width: 60px; height: 60px; margin-right: 10px;">
                                        <!-- <img src="./image2.png" alt="Image" width="107" height="120"> -->

                                        <img src="cid:image_cid" alt="Image" width="107" height="120">
                                    </td>
                                    <td style="color: white; font-family: 'Arial';">
                                        <h1 style="margin: 0; margin-left: 10px; font-weight: normal;">OPPORTUNITY
                                            <br>INTELLIGENCE</h1>
                                    </td>
                                </tr>
                            </table>
                            <H2 id="rn"
                                style="color: white; font-family: 'Arial'; font-weight: normal; margin-left: 40px;">
                                Refresh
                                Notification</H2>
                        </td>
                    </tr>
                </table>

                <!-- Mail body starts -->

                <p style="font-family: Arial, Helvetica, sans-serif;">December 06, 2023</p>
                <h1 style="font-family: Arial, Helvetica, sans-serif; color: #ec008c; font-weight: normal;">Sales &
                    Marketing Enablement Data Refreshed thru October 2023</h1>

                <p
                    style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: large; color: #9579d3; font-weight: normal;">
                    Sales and Marketing Enablement data products refreshed with data thru October 2023</p>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: medium; font-weight: bold;">Data Refresh
                    Update</p>

                <ul>
                    <li style="font-family: Arial, Helvetica, sans-serif;">UniData Monthly Refresh with data thru
                        October 2023 is complete. </li>
                </ul>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: 15;">Please reach out to <a
                        href="mailto:sme.oi@cotiviti.com" id="us">us</a> to get the latest updates on Sales and
                    Marketing Enablement data products.</p>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: medium;">Best Regards,</p>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: large; color: #9579d3;">Opportunity
                    Inetlligence</p>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: small; font-style: italic;">Proprietary
                    and Confidential — For Internal Use Only</p>

                <p style="font-family: Arial, Helvetica, sans-serif; font-size: small; font-style: italic;"> <br></p>
            </td>
        </tr>

    </table>

    <br>


    <!-- second table starts -->

    <table border="0" cellspacing="0" cellpadding="0" width="650px" style="border-collapse: collapse;">
        <tr>
            <td
                style="border-width: 1px; border-style: solid; border-color: gray; border-radius: 0px; padding: 2px; padding-top: 10; margin: 10px;">
                <h1 style="margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif;">
                    <span style="color: #31006f;">C</span>
                    <span style="color: #9579d3;">O</span>
                    <span style="color: #31006f;">T</span>
                    <span style="color: #ec008c;">I</span>
                    <span style="color: #31006f;">V</span>
                    <span style="color: #31006f;">I</span>
                    <span style="color: #31006f;">T</span>
                    <span style="color: #31006f;">I</span>
                </h1>
            </td>
        </tr>
        <tr>
            <td
                style="border-width: 1px; border-style: solid; border-color: gray; border-radius: 0px; padding: 2px; margin: 10px;">
                <p style="font-family: Arial, Helvetica, sans-serif; font-size: small; color: rgb(92, 90, 90);">
                    CONFIDENTIALITY NOTICE: This email message and any attachments accompanying it may contain
                    confidential information intended solely for the use of the addressee. If you have received this
                    communication in error, please notify me immediately by a reply email or by phone, and permanently
                    delete the original email and any attachments from all storage devices without retaining a copy.</p>
            </td>
        </tr>

    </table>


</body>

</html>
""".format(image_cid)


message.attach(MIMEText(html_content, 'html'))

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    # Send the email
    server.sendmail(sender_email, recipients, message.as_string())