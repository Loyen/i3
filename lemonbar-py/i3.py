#!/bin/python

import shell
import json

def get_workspaces():
	workspaces_json = shell.exec("i3-msg -t get_workspaces")
	workspaces = json.loads(workspaces_json)
	return workspaces

def get_current_workspace():
	workspaces = get_workspaces()
	for workspace in workspaces:
		if workspace['focused'] == True:
			return workspace

