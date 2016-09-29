#!/bin/bash

def text_color(color):
	return "%{F"+str(color)+"}"

def background_color(color):
	return "%{B"+str(color)+"}"

def border_color(color):
	return "%{U"+str(color)+"}"

def action(action, str):
	return "%{A:"+str(color)+"}"+str(str)+"%{A}"

def position(name):
	if name == "right":
		return "%{r}"
	elif name == "center":
		return "%{c}"

	return "%{l}"
