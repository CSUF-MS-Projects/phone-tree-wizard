from twilio.twiml.voice_response import Gather, VoiceResponse, Say
#from url import callback

class ParseSpeech(object):
    def parse(self, company):
        pass

class Twilio(ParseSpeech):
    def __init__(self):
        super(Twilio, self).__init__()

    def parse(self, company):
        print("parsing speech using Twilio now!! ")
        response = VoiceResponse()
        gather = Gather(input='speech', action='wrong')
        response.append(gather)
        print(response)
