https://docs.python.org/3/library/smtplib.html
https://docs.python.org/3/library/datetime.html


https://www.pythonanywhere.com/

A Note About the Next Lesson: Google SMTP Port
In the next lesson, I'll show you how to send email using the smtplib module and Python. If you are getting the error Connection unexpectedly closed, it might be due to a number of things. You can come back to this lesson to debug.


1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"



Below are steps specific to users sending email from Gmail addresses.

2. Go to https://myaccount.google.com/

Select Security on the left and scroll down to How you sign in to Google.

Enable 2-Step Verification



3. Click on 2-Step Verification again, and scroll to the bottom.

There you can add an App password.

Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.

COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.

Use this App password in your Python code instead of your normal password.



4. Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)





let's say that we have a sender Angela gmail.com and a recipient Timmy at Yahoo dot com.

Now in order to send this email from my Gmail account to another email account, what happens behind

the scene is that there's a Gmail mail server which will receive my message and then there's a Yahoo

Mail server which will store the message until Timmy logs on to his computer and logs on to Yahoo dot

com, which downloads the email from the Yahoo Mail server.

So this email is going to move between all of these steps.

And in order to do this, it relies on something called SMTP, the simple mail transfer protocol.

And this contains all of the rules that determine how an email is received by mail servers passed onto

the next mail server and how email can be sent around the Internet.