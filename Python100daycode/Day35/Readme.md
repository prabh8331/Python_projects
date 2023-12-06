What is API Authentication:
Some data is very resource heavy and need lot of cost to create due to which some data required cost with it

https://home.openweathermap.org/ 
user - prabh8331@gmail.com



sms service - 
https://www.twilio.com/try-twilio


Environment variables 

why use environmet variable - 
1. for the convenience (we don't watn to change the code) but we change the auth key or server ,etc then we use environment variables
2. Security - when we upload our code in some online source we don't want anyone to have access of our key or password , 


```bash
env  # to check the list of all environment variables present 

export twillio_account_sid=fjadsoifjasdfapofguygajoi23dsf
export twillio_auth_token=blablablayourowntoken
export OWM_api_key=blablablayourownapikey
export my_phone_no=+9152452352345

env  # to check if it is added or not


## pass environment varaiable before running the python script-- put this in bashfile

export twillio_account_sid=fjadsoifjasdfapofguygajoi23dsf; export twillio_auth_token=blablablayourowntoken; export OWM_api_key=blablablayourownapikey; export my_phone_no=+9152452352345 python3 main.py

```