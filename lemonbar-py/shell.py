#!/bin/python

import subprocess

def exec(cmd):
	return str(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True).stdout.read()).strip()

