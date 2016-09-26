#!/bin/bash

def text_color(color, str):
	return "%{F"+str(color)+"}"+str(str)

def background_color(color, str):
	return "%{B"+str(color)+"}"+str(str)

def border_color(color, str):
	return "%{U"+str(color)+"}"+str(str)

def action(action, str):
	return "%{A:"+str(color)+"}"+str(str)+"%{A}"
