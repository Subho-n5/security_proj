#Python script to check active URLs either using single URL or file of URL


#!/usr/bin/python3

import os,sys

def active_stats(website):
	q1 = ("ping -q -c 1 %s 2> /dev/null 1> /dev/null" %website) #Sending both ping result and error to /dev/null to avoid unnecessary printing
	status = os.system(q1)#Storing the ping status 
	if status == 0 :
		q2 = ("ping -c 1 %s | head -1 | cut -d ' ' -f3 | sed 's/^.//' " % website)#Using the IP resolved from ping command and formatting the output using cut and sed is removing the first bracket
		ip = os.popen(q2).read()#Storing the output of the command in a variable rather than executing and printing the command directly
		ip = ip[:-2]#Removing the last 2 characters(One is ')' from ping command and other is '\n' from the command execution )
		print(ip+ " is the ip of " +website)
	else :
		print("%s : is an invalid website." % website)


if len(sys.argv) == 3:#Checking number of arguments : file name, flag , input
	if sys.argv[1] == '-u':
		active_stats(sys.argv[2])
	elif sys.argv[1] == '-f':
		with open(sys.argv[2]) as file:
			sites = file.readlines()
		for x in sites:
			x = x[:-1]
			active_stats(x)
	else :
		print("Wrong Flag!! Use: filename -h  -> For help")

elif len(sys.argv) == 2 and sys.argv[1] == '-h':
	print("Format to use: python3 active_url.py flag [optional]")
	print("-u  -> For a single URL")
	print("-f  -> For a file with URLs")
	print("-h  -> For help")
else:
	print("Enter appropriate number of arguments! ")
	print("Use: filename -h  -> For help")

