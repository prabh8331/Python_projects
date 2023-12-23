# Gmail API to retrieve Data

## Challenge: Managing a Large Volume of Gmail Emails

I encountered a significant challenge when faced with an overwhelming influx of emails in my Gmail account. The sheer volume of messages made it increasingly difficult to efficiently manage and optimize my Gmail experience.

## Issue: Email Overload

As the number of emails continued to grow, I found it challenging to keep track of important messages, leading to decreased productivity and potential oversight of crucial information. The conventional Gmail interface offered limited tools for organizing and managing emails at scale, especially when dealing with thousands of messages.

### Enable Gmail API
* Go to the Google Cloud Console
  * Login with your gmail account
  * Create a New Project
    * Click on the project dropdown in the upper right corner.
    * Click on "New Project."
    * Enter a name for your project, and click "Create" and select Project
  * Enable the Gmail API
    * In the left navigation menu, click on "APIs & Services" > click on "Enable APIs & services"
    * Go to "Google Workspace" and click "Gmail API" and "Click on "ENABLE"
  * click on "Create credentials"
    1. Credential Type
       1. Which API are you using? -- Gmail API
       2. and select User data and NEXT
    2. OAuth Consent Screen
       1. App information 
          1. App name --> pythonapp 
          2. user support email --> youemail@gmail.com
       2. App Logo --> skip
          1. Developer contact information --> youemail@gmail.com
    3. Scopes
       1. Click on --> ADD OR REMOVE SCOPES
       2. window will popup --> search for gmail.readonly (this will show - https://www.googleapis.com/auth/gmail.readonly) --> check and click on UPDATE
          1. save and continue
    4. OAuth Client ID
       1. Application app --> Desktop app
       2. Name --> "Desktop client 1"
       3. click on "CREATE"
       4. click on "DOWNLOAD" it will download json file

### Install Libraries for this project

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Python to fetch data
Refer my pyhton code to fetch data

### Categorize domain in Excel
Refer my Domain_analysis.xlsx file for my analysis