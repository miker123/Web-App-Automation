#!/usr/bin/env python
#Author: Mike R
#Date: 1/13/2016
#Run hosts command to get full DNS lookup

import subprocess

#Ask user for site
site=raw_input("Target site:")

f = open('hostResult.txt', 'w')

#get all host entries for the site
p = subprocess.Popen(['host', '-a', site], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out 
f.write(out)

#Other options instead of -a can be found at http://www.computerhope.com/unix/host.htm
