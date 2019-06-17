#! /usr/bin/python

import glob

files = glob.glob('sandbox/*.txt')

files.sort()

print(files)

for f in files:
	print(tuple(open(f))[0][::-1])
