#!/usr/bin/env python 

def dayofweek(year,month,day):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	a = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}
	if month < 3 :
		year = year - 1
	answer = (year + year / 4 - year / 100 + year / 400 + t[month-1] + day ) 
	answer = answer % 7
	return a[answer]

print "12/05/2000 is " + dayofweek(2000,05,12)
print "01/01/2012 is " + dayofweek(2012,01,01)
print "01/04/2012 is " + dayofweek(2012,04,01)
