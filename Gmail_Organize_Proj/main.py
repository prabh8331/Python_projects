import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set the scope to access Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    token_path = 'token.json'

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_emails(service):
    # Call the Gmail API
    results = service.users().messages().list(userId='me',maxResults=100).execute()
    messages = results.get('messages', [])

    while 'nextPageToken' in results:
        page_token = results['nextPageToken']
        results = service.users().messages().list(userId='me', maxResults=100, pageToken=page_token).execute()
        messages.extend(results.get('messages', []))

    import json

    file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/mail_id.json"
    
    with open(file_path, 'w') as json_file:
        json.dump(messages, json_file, indent=2)

    with open(file_path, 'r') as json_file:
        messages = json.load(json_file)

    senders = []
    subjects = []
    i=1
    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            sender = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'From'][0]
            # try:
            #     subject = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject'][0]
            # except IndexError:
            #     subject = " "
            print(i)
            i+=1
            senders.append(sender)
            # subjects.append(subject)
    
    data = {"sender": senders, "subject":subjects}

    file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data.json"
    

    with open(file_path, 'w') as json_file:
        json.dump(senders, json_file, indent=2)

    senders = []
    for i in range(17467, 51030):
        message = messages[i]
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        sender = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'From'][0]
        print(i)
        senders.append(sender)

    # 17500
    # 23254
        
    file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data2.json"

    with open(file_path, 'w') as json_file:
        json.dump(senders, json_file, indent=2)


# 17500
# 23254
# 30063




senders = []
for i in range(30063, 51029):
    message = messages[i]
    try: 
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        sender = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'From'][0]
    except:
        sender = " "
    print(i)
    senders.append(sender)


 
file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data4.json"
with open(file_path, 'w') as json_file:
    json.dump(senders, json_file, indent=2)






file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data.json"
with open(file_path, 'r') as json_file:
    data1 = json.load(json_file)

file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data2.json"
with open(file_path, 'r') as json_file:
    data2 = json.load(json_file)

file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data3.json"
with open(file_path, 'r') as json_file:
    data3 = json.load(json_file)

file_path = "C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/data4.json"
with open(file_path, 'r') as json_file:
    data4 = json.load(json_file)

data = data1+data2+data3+data4

import pandas as pd

df = pd.DataFrame(data)

csv_file_path = 'C:/Users/prabh/OneDrive/Desktop/Gmail data pull method/output.csv'

df.to_csv(csv_file_path, index=False, header=False)

if __name__ == '__main__':
    service = authenticate_gmail()
    get_emails(service)
