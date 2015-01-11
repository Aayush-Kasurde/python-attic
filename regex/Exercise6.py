#!/usr/bin/env python
# Exercise 6 - repeatition cases 

import re

line = "123456"

#matchObj = re.search(r'\d{3}', line, re.M|re.I)   # Match exactly 3 digits
#matchObj = re.search(r'\d{3,}', line, re.M|re.I)  # Match 3 or more digits
matchObj = re.search(r'\d{3,5}', line, re.M|re.I)  # Match 3, 4, or 5 digits

if matchObj:
    print "matchObj.group() : ", matchObj.group()
else:
    print "No Match found"
