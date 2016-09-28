#!/bin/python

import time

# Custom libs
import i3
import shell
import lemonbar

def block_workspaces(item, settings):
	workspace_items=[]

	workspaces=i3.get_workspaces()
	for workspace in workspaces:
		workspace_item={}
		if workspace["focused"] == True:
			workspace_item["foreground"] = item["active_foreground"]
			workspace_item["background"] = item["active_background"]

		workspace_item["output"] = workspace["name"]

		workspace_items.append(workspace_item)

	item["items"] = workspace_items
	return item

def block_volume(item, settings):
	volume = shell.exec("pamixer --get-volume")
	item["output"] = str(volume)+"%"

	return item

def block_time(item, settings):
	item["output"] = time.strftime(item["format"])
	return item

