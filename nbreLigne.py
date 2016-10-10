#!/usr/bin/python

import os
import sys

repertory = sys.argv[1]
#print repertory
def file_len(fname):
	i = 0
	file = open(fname)
	for line in file:
		i+=1
	return i

count = 0
for path, dirs, files in os.walk(repertory):
	for filename in files:
		count += file_len(os.path.join(path,filename))

print count	
