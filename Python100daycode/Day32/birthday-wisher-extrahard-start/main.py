##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
import smtplib


letters = []

for i in range(1,4):
    with open(f"Python100daycode/Day32/birthday-wisher-extrahard-start/letter_templates/letter_{i}.txt") as letter:
        letters.append(letter.read())

recipients = pandas.read_csv("Python100daycode/Day32/birthday-wisher-extrahard-start/birthdays.csv")

now = dt.datetime.now()

year=now.year
month=now.month
day=now.day

# today = dt.datetime(year=year , month=month , day=day)
# print(today)

today= f'{month}_{day}'

my_email = "prabh8331@gmail.com"
password = "rpwawjquklucwafx"

for (index, row) in recipients.iterrows():
    # birthday=dt.datetime(year=row.year , month=row.month , day=row.day)
    # print(birthday)
    birthday=f'{row.month}_{row.day}'
    if today == birthday:
        body = random.choice(letters)
        body= body.replace("[NAME]",row.names)
        # print(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                            to_addrs=row.email,
                            msg=f"Subject:Happy Birthday {row.names}\n\n{body}")


