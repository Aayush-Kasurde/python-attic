#!/usr/bin/env python
# Exercise 1

import re

line = "Cats are smarter than dogs.Abc";

matchObj = re.search(r'(.*) are (.*) than', line, re.M|re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No Match found"
