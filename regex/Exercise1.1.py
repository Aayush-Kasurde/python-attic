#!/usr/bin/env python
# Exercise 7 - special character

import re

#line = "Python"
line = "a fox in fire"

matchObj = re.search(r'[Pp]ython', line)
matchObj = re.search(r'[aeiou]', line)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
else:
    print "No Match found"
