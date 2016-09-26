#!/bin/python

def thisfunctiondoexist():
	print("Hello world!")

try:
	fnname="thisfunctiondonotexist()"
	fnname="thisfunctiondoexist()"
	print(fnname)
	eval(fname)
except:
	print("what the fuck")
