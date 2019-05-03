"""
Purpose:  Initialize all parent-to-child classes (inheritance)
"""


# import libraries
import outboundCall
import parse
import treeDiagram

class Company(object):
    def __init__(self, phoneNum=None, companyName=None):
        self.phoneNum = phoneNum
        self.companyName = companyName
        self.outbound_method = outboundCall.OutboundCall()
        self.parse_method = parse.ParseText()
        self.treeDiagram_method = treeDiagram.drawTreeDiagram()

    def display(self):
        pass

    def dial(self, company):
        self.outbound_method.dial(company)

    def parse(self, company, text):
        return self.parse_method.parse(company, text)

    def drawDiagram(self, company):
        self.treeDiagram_method.drawDiagram(company)

class RegularCompany(Company):
    def __init__(self,
                 phoneNum=None,
                 companyName=None,
                 outbound_method=None,
                 parse_method=None,
                 treeDiagram_method=None):
        super(RegularCompany, self).__init__(phoneNum, companyName)
        self.outbound_method = outbound_method
        self.parse_method = parse_method
        self.treeDiagram_method = treeDiagram_method

    def display(self):
        print("Calling company: " + self.companyName + "   // Phone Number:  " + self.phoneNum)