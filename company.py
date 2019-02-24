import outboundCall

class Company(object):
    def __init__(self, phoneNum=None, companyName=None):
        self.phoneNum = phoneNum
        self.companyName = companyName
        self.outbound_method = outboundCall.OutboundCall()

    def display(self):
        pass

    def dial(self, company):
        self.outbound_method.dial(company)


class RegularCompany(Company):
    def __init__(self, phoneNum=None, companyName=None, outbound_method=None):
        super(RegularCompany, self).__init__(phoneNum, companyName)
        self.outbound_method = outbound_method

    def display(self):
        print("Regular company " + self.companyName + "   ----  " + self.phoneNum)