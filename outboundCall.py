class OutboundCall(object):
    def dial(self, company):
        pass

class Twilio(OutboundCall):
    def __init__(self):
        super(Twilio, self).__init__()

    def dial(self, company):
        print("Dialing with Twilio  " + company.phoneNum)

class GoogleVoice(OutboundCall):
    def __init__(self):
        super(GoogleVoice, self).__init__()

    def dial(self, company):
        print("now dialing with GoogleVoice " + company.phoneNum)


