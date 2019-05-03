import os
from twilio.rest import Client
from twilio.twiml.voice_response import Dial, VoiceResponse, Say, Gather



TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_API = os.environ.get('TWILIO_API')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWIML_INSTRUCTIONS_URL = "https://2cf79e46.ngrok.io/parsing"


client = Client(TWILIO_API, TWILIO_AUTH_TOKEN)

class OutboundCall(object):
    def dial(self, company):
        pass

class Twilio(OutboundCall):
    def __init__(self):
        super(Twilio, self).__init__()

    def dial(self, company):
        print("Dialing " + company.phoneNum)
        # set the method to "GET" from default POST
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(
            to=company.phoneNum,
            from_=TWILIO_PHONE_NUMBER,
            url=TWIML_INSTRUCTIONS_URL
        )

class GoogleVoice(OutboundCall):
    def __init__(self):
        super(GoogleVoice, self).__init__()

    def dial(self, company):
        print("now dialing with GoogleVoice " + company.phoneNum)


