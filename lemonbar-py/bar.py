#!/bin/python

# Custom libs
import blocks
import json

def render(item, settings):
	command=item["command"]
	try:
		return eval("blocks.block_"+command+"(item, settings)")
	except:
		return ""

def main():
	config_json = open("config.json", "r")
	config = json.loads(config_json.read());

	output=""
	for item in config["items"]:
		output+=render(item, config["settings"])

	print(output)

if __name__ == "__main__":
	main()
