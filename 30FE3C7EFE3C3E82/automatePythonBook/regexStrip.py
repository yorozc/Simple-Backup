#! python3
# regexStrip.py - does the same thing as strip but with regex

import re

#if one args passed, white space characters removed from begin and end
def regexStrip(word, subWord=""):
    if len(subWord) != 0:
        wordRegex = re.compile(fr'{subWord}')
        fixed = wordRegex.sub('', word)
    else:
        wordRegex = re.compile(r'[a-zA-Z0-9].*')
        fixed =  wordRegex.search(word).group()
    return fixed

print(regexStrip("      yep   another    "))

print(regexStrip("     testing another one this time with even more spaces   f"))
print(regexStrip("---Pyt-hon---", "-"))

text = "---I want this word gone----t"
cleanText = text.strip("-t")
print(f"{cleanText}")