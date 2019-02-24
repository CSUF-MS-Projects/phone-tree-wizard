from twilio.rest import Client
from twilio.twiml.voice_response import Dial, VoiceResponse, Say


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

    # def dial(self, company):
    #     print("Dialing with Twilio  " + company.phoneNum)

class GoogleVoice(OutboundCall):
    def __init__(self):
        super(GoogleVoice, self).__init__()

    def dial(self, company):
        print("now dialing with GoogleVoice " + company.phoneNum)


