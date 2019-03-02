import outboundCall
import parseSpeech

class Company(object):
    def __init__(self, phoneNum=None, companyName=None):
        self.phoneNum = phoneNum
        self.companyName = companyName
        self.outbound_method = outboundCall.OutboundCall()
        self.parse_method = parseSpeech.ParseSpeech()

    def display(self):
        pass

    def dial(self, company):
        self.outbound_method.dial(company)

    def parse(self, company):
        self.parse_method.parse(company)


class RegularCompany(Company):
    def __init__(self, phoneNum=None, companyName=None, outbound_method=None, parse_method=None):
        super(RegularCompany, self).__init__(phoneNum, companyName)
        self.outbound_method = outbound_method
        self.parse_method = parse_method

    def display(self):
        print("Regular company " + self.companyName + "   ----  " + self.phoneNum)