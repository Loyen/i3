#!/bin/python

# Custom libs
import blocks
import json

def render(item, settings):
	try:
		if item["command"]:
			command=item["command"]
			del item["command"]
			try:
				item = eval("blocks.block_"+command+"(item, settings)")
			except:
				pass
	except:
		pass

	output=""

	try:
		if item["items"]:
			for item_item in item["items"]:
				output+=render(item_item, settings)
	except:
		try:
			if item["output"]:
				output+=item["output"]
		except:
			pass

	return output

def main():
	config_json = open("config.json", "r")
	config = json.loads(config_json.read());

	output=""
	for item in config["items"]:
		output+=render(item, config["settings"])

	print(output)

if __name__ == "__main__":
	main()
