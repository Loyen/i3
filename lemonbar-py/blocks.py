#!/bin/python

import time

# Custom libs
import i3
import shell
import lemonbar

def block_workspaces(item, settings):
	output=""

	workspaces=i3.get_workspaces()
	for workspace in workspaces:
		if workspace["focused"] == True:
			output+=">"

		output += workspace["name"]

		if workspace["focused"] == True:
			output+="<"

	return output

def block_volume(item, settings):
	volume = shell.exec("pamixer --get-volume")
	return str(volume)+"%"

def block_time(item, settings):
	return time.strftime(item["format"])

