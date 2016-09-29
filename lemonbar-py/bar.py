#!/bin/python

import json

# Custom libs
import blocks
import lemonbar

def render(item, settings):
	output=""
	if "output" in item:
		if "foreground" in item:
			output+=lemonbar.text_color(item["foreground"])

		if "background" in item:
			output+=lemonbar.background_color(item["background"])

		if "position" in item:
			output+=lemonbar.position(item["position"])

		output+=item["output"]

	return output

def parse(item, settings):
	if "command" in item:
		command=item["command"]
		del item["command"]
		try:
			item = eval("blocks.block_"+command+"(item, settings)")
		except:
			pass

	output=""

	if "items" in item:
		items = item["items"]
		del item["items"]
		item_settings=settings
		for setting,value in item:
			item_settings[setting] = value

		for item_item in list.items:
			output+=parse(item_item, item_settings)
	elif "output" in item:
			output+=render(item, settings)

	return output


def main():
	#while True:
		config_json = open("config.json", "r")
		config = json.loads(config_json.read());

		output=""
		for item in config["items"]:
			output+=parse(item, config["settings"])

		print(output)

if __name__ == "__main__":
	main()
