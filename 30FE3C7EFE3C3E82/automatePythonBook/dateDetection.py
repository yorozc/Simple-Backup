#! python3
# dateDetection.py - detects data and checks if it is a valid date

import re

# DD/MM/YYYY
# days - 01 to 31, months - 01 to 12, years - 1000 to 2999


dateRegex = re.compile(r'''
                    ^(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/
                    (0[1-9]|1[0-2])\/
                    (1[0-9][0-9][0-9]|2[0-9][0-9][0-9])$
                    ''',re.VERBOSE)

date = dateRegex.search('21/01/2025').group()

print(date)
