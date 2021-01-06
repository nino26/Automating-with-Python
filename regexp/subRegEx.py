# import re
#
# namesRegex = re.compile(r'Agent \w+')
#
# print(namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.'))



import pyperclip,re

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)
