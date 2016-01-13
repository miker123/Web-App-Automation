#!/usr/bin/env python
#Author: Mike R
#Date: 1/13/2016
#Run WhoIS command from command line to get website WhoIS Record
#Works on Linux by default. 
import subprocess

#Ask user for site
site=raw_input("Target site:")

f = open('whoisCMD.txt', 'w')

#get all whois entries for the site
p = subprocess.Popen(['whois', site, 'ANY'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out 
f.write(out)
