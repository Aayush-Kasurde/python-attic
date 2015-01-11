#!/usr/bin/python

import re

# ?
#line = "Python"   # Match
#line = "Pythons" # Match
#line = "Pytho"  # No Match
#line = "python"  # No Match
#line = "pythons"  # No Match

# *
#line = "Pythons" # match
#line = "Pythonss" # match
#line = "pythonss" # no match
#line = "Python" # match

# +
#line = "Python" # no match
#line = "Pythons" # match
#line = "Pythonsssssssssssss" # match
#line = "python" # no match
#line = "pythons" # no matchss

#matchObj = re.search(r'Pythons?', line) # where s is optional
#matchObj = re.search(r'Pythons*', line) # where s is 0 or more
matchObj = re.search(r'Pythons+', line) # where s is 1 or more

if matchObj:
    print "matchObj.group() --> ", matchObj.group()
else:
    print "No match found"
