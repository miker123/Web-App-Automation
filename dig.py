#!/usr/bin/env python
#Author: Mike R
#Date: 12/9/2015
#Edited: 1/13/2016
#Run DIG command to get full data from website

import subprocess

#Ask user for site
site=raw_input("Target site:")

f = open('digResult.txt', 'w')

#get all dig entries for the site
p = subprocess.Popen(['dig', site, 'ANY'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out 
f.write(out)

#Transfer entire zone file from the master name server to secondary name servers
p1 = subprocess.Popen(['dig', site, 'AXFR'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out1, err1 = p1.communicate()
print out1
f.write(out1)

#Potential for script:
#Run different options instead of AXFR. Other options can be found at https://en.wikipedia.org/wiki/List_of_DNS_record_types
