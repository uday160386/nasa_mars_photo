# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'TWILIO_SID'
auth_token = 'TWILO_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='', # number which you will purchase from twilio
                              body='body',
                              to=''# give your mobile number which is registered intwilio
                          )

print(message.sid)
