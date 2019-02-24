

# from abc import ABCMeta, abstractmethod
#
# class Information:
#     __metaclass__ = ABCMeta
#
#     def __init__(self, phoneNumber, companyName):
#         self.phoneNumber = phoneNumber
#         self.companyName = companyName
#
#     @abstractmethod
#     def info(self): pass
#
#     def setPhoneNumber(self):
#         phone_number = input("Enter phone number to call: ")
#         return phone_number
#
#     def getPhoneNumber(self):
#         phoneNumber = self.setPhoneNumber()
#         return phoneNumber
#
#     def getCompanyName(self):
#         company_name = input("Enter company name: ")
#         return company_name
#
#
# class RegularInformation(Information):
#     def __init__(self):
#             self.getPhoneNumber()
#             self.getCompanyName()
#
# # class RegularInformation(Information):
# #     def info(self):
# #         phone_number = input("Enter phone number to call: ")
# #         return phone_number
# #
# #     def info(self):
# #         company_name = input("Enter company name: ")
# #         return company_name