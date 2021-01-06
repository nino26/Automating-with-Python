# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#          return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
#
# #
# # message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# # for i in range(len(message)):
# #     chunk = message[i:i+12]
# #     if isPhoneNumber(chunk):
# #         print('Phone number found: ' + chunk)
# # print('Done')
# import re #importing the regular expression lib
#
# phoneNumRegex = re.compile(r'(\d){3}-(\d){3}-(\d){4}')
# # phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #regex object
#
# mo = phoneNumRegex.search('My number is 415-343-4533.')
# print('Phone number found: '+ mo.group())


import re

numRegex = re.compile(r'\d{1-3}')
mo = numRegex.sub('X', '12 drummers, 11 pipers, 5 rings, 3 hens')

print(mo)
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
#
# print(mo.group(1))


# phoneNumRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-6446'))

# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman stole the election')
# print(mo1.group())
