---

# MMS, a photo of MARS: using NASA Mars Rover Photo API and Twilio

Knowing about other planet especially MARS is always interesting. I always wonder on environment, landscape etc.,
Think about , What if we can get few images from space? Yes, NASA getting photos taken by Rover from MARS and storing internally. These images are shared through API's that are exposed publicly. Any developer or enthusiast can consume and use it for a purpose.
Information on NASA api's is available at [https://api.nasa.gov/index.html#getting-started]

## What are Mars`s Rover Photos API?
These API's gives a response with images that are collected by NASA`S Curiosity, Opportunity and Spirit rovers. We can use queries to fetch data and filtered it by date, region , camera and angle.
Example query : [https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos](https://www.blogger.com/u/2/blog/post/edit/6497426378157298179/7900605512514296005#)
Note: please register for access ket before trying nasa api's

## What Next?
Let's  design and develop an application that will send photos of mars to your mobile number.

## Design:

> Send SMS from Mobile to Twilio .
> Twilio will call a web-service which is hosted in local environment.
> Post request will be triggered and response will be generated
> Message with image will be send to mobile number.

## Prerequisites:
> Install python 2.7 or 3.2. Check if the python is installed using a command Python3 -V
> Install twilio, flask, and request modules using command sudo python3.7 pip install requests==2.13.0 twilio==6.0.0 flask==0.12.1

Getting NASA API access Key : Register at [https://api.nasa.gov/index.html#apply-for-an-api-key](https://www.blogger.com/u/2/blog/post/edit/6497426378157298179/7900605512514296005#)
The NASA developer API Key will be sent to you registered email id on a successful registration. Example: "2jVyoshYV4YKDQRb47365287364hfjdjfdhsgjhJ6QInjZ6sPNWg

## Twilio Integration:
1.Open Twilio Website [https://www.twilio.com/try-twilio](https://www.blogger.com/u/2/blog/post/edit/6497426378157298179/7900605512514296005#) and complete a trial registration.
3. Login with the credentials and Dashboard page will be displayed.

3. Click on Get Number and finish buying process. Also select the checkbox for all required features.
4. Now click on Phone number link and Twilio Phone number will be displayed. This means Twilio phone number is available for you.
5. Now, go to dashboard again and get the Twilio Acccount SID and AUTH Token to use it in code.
6. Finally, to get SMS/MMS, you need to register your mobile numbers in Twilio at Phone Numbers->Verified Caller Id`s->Add your number and give OTP to complete the process.

## Implementation:
### Calling NASA API:

filename:mars.py
a function name  get_url_of_photo is created

```import requests
from random import choice
rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
def get_url_of_photo(sol, api_key='NASA API KEY'):
params = { 'sol': sol, 'api_key': api_key }
response = requests.get(rover_url, params)
response_dictionary = response.json()
photos = response_dictionary['photos']
return choice(photos)['img_src']
```


Call SMS API from Twilio:
filename: app.py
```import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from mars import get_mars_photo_url 
app = Flask(__name__)
account_sid = '' #replace with twili0 account sid
auth_token = '' # replace with twilio auth token
client = Client(account_sid, auth_token)
@app.route('/sms', methods=['POST'])
def inbound_sms():
message_body = request.form['Body']
resp = MessagingResponse()
if message_body.isdigit():
response_message = 'Taken {} Martian solar days into the journey.' \
.format(message_body)
photo_url = get_url_of_photo(message_body)
print(photo_url)
msg = Message()
msg.body(response_message)
msg.media(photo_url)
resp.append(msg)
else:
msg = Message().body('Text a number of solar days into the rover\'s journey.')
resp.append(msg)
return str(resp)
if __name__ == '__main__':
app.run()
```



**How to Run?**
```Run app.py file using command python3.7 app.py```

An web service instance will be started and running on port 5000
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

But, we need to expose the local instance to public, where twilio can access sms api. To do this we are using ngrok.

From console , run the command .
`ngrok http 5000`
This will expose local instance to public.
Now configure, the twilio number with forwarding url like below.
Go to Twilio Dashboard. Select Phonenumber.
Go to Configure section. Refer to Messaging section.

Save the public url in "A MESSAGE COMES IN" text box. Don`t forgot to append "/sms" in the end of url.

Now you can send sms Twilio number and the response to your mobile number is a Image which took in Mars.
Result:### 
I am sending a message to Twilio number with number of day (Photos are organized by the sol (Martian rotation or day) on which they were taken, counting up from the rover's landing date. )

### Source:
I took this example from Twilio website (https://www.twilio.com/blog/2017/04/texting-robots-on-mars-using-python-flask-nasa-apis-and-twilio-mms.html) and tried and documented more information.


