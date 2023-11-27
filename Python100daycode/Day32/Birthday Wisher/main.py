import smtplib

my_email = "prabh8331@gmail.com"
password = "rpwawjquklucwafx" ##go to security in google setting go to app password and create new app and use the password given

with open("C:/Users/prabh/OneDrive/Desktop/google_app_pass.txt") as login:
    password=login.readlines()[1].strip()

print(password)

# connetion = smtplib.SMTP("smtp.gmail.com", 587)

# connetion.starttls()

# connetion.login(user=my_email, password=password)

# connetion.sendmail(from_addr=my_email, 
#                    to_addrs="kkomalpreet0000@gmail.com", 
#                    msg="Subject:I love you\n\nYou are my everything jaan ji.")

# connetion.close()


with smtplib.SMTP("smtp.gmail.com", 587) as connection:

    connection.starttls()

    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email, 
                    to_addrs="kkomalpreet0000@gmail.com", 
                    msg="Subject:I love you\n\nYou are my everything jaan ji.")



# import datetime as dt

# now = dt.datetime.now()
# year=now.year
# month=now.month
# weekday=now.weekday()

# print(now.year)
# print(month)
# print(weekday)

# print(now)


# if year == 2023:
#     print("its cold today")


# date_of_birth = dt.datetime(year=1996 , month=6 , day=20)

# print(date_of_birth)