#!/usr/bin/env python
#Author: Mike R
#Date: 1/14/2016
#Run WGET command to do automated spidering

import subprocess

#Ask user for site or can provide list of sites to scan.
site=raw_input("Target site:")

#provide full path for the file so it can download to proper directory
f = open('wgetResult.html', 'w')

#Won't provide any output that can be printed. Will write all data to the HTML file. 
p = subprocess.Popen(['wget', '-O', f , '-r', site, '-l', '0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Will want to change the options, but this will recursively scan all the sites to an infinite depth
