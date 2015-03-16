import sys 

try:
	import os,stat,time,hashlib,optparse,subprocess,fnmatch,re,dbus
	
except ImportError,msg:
	sys.exit("Error : The required modules %s is missing "%(str(msg).split()[-1]))


