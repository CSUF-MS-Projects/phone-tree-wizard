import company
import outboundCall
import parseSpeech



input_company = input("Enter company name: ")
input_phone = input("Enter phone number to dial: ")

# initial set up
c1 = company.RegularCompany(phoneNum=input_phone, companyName=input_company, outbound_method=outboundCall.Twilio(), parse_method=parseSpeech.Twilio())
c1.display()

# call various outbound methods
print('\n')
c1.dial(c1)
print("outro")
c1.parse(c1)

# switch outbound_method to GoogleVoice
c1.outbound_method = outboundCall.GoogleVoice()
c1.dial(c1)