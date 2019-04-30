import company
import outboundCall
import parse

input_company = input("Enter company name: ")
input_phone = input("Enter phone number to dial: ")

# initial set up
c1 = company.RegularCompany(phoneNum=input_phone,
                            companyName=input_company,
                            outbound_method=outboundCall.Twilio(),
                            parse_method=parse.parse_PS())
c1.display()

# call various outbound methods
print('\n')
c1.dial(c1)

text = "Thank you for calling walmart.com for Walmart and Sam's Club store locations questions about our source savings catcher program or the Walmart credit card, press 1 to track a walmart.com order, press 2 for all other walmart.com related questions, press 3. To hear this message again, press star."
c1.parse(c1, text)

#  switch outbound_method to GoogleVoice
c1.outbound_method = outboundCall.GoogleVoice()
c1.dial(c1)
