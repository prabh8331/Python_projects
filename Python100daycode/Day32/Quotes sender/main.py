import random
import smtplib
import datetime as dt
import time

time.sleep()

my_email = "prabh8331@gmail.com"
password = "rpwawjquklucwafx" ##go to security in google setting go to app password and create new app and use the password given


with open(file="Python100daycode/Day32/Quotes sender/quotes.txt") as data:
    quotes = data.readlines()
    quote = random.choice(quotes).strip()

now = dt.datetime.now()

weekday = now.weekday()

print(weekday)
print(type(weekday))

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="prabh8331@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n{quote}")
