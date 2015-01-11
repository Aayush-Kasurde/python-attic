#!/usr/bin/env python
# Exercise 7 - special character

import re

#line = "A123456" # 1 and 2
line = "asdas vvbbb"
#line = "_asdas"

#matchObj = re.search(r'\d', line, re.M|re.I)  # Match [0-9]
#matchObj = re.search(r'\D', line, re.M|re.I)  # Match non [0-9]
#matchObj = re.search(r'\s(.*)', line, re.M|re.I)  # Match whitespace
#matchObj = re.search(r'\S', line, re.M|re.I)  # Match nonwhitespace
matchObj = re.search(r'\w', line, re.M|re.I)  # Match [A-Za-z0-9_]
#matchObj = re.search(r'\W', line, re.M|re.I)  # Match non [A-Za-z0-9_]

if matchObj:
    print "matchObj.group() : ", matchObj.group()
else:
    print "No Match found"
