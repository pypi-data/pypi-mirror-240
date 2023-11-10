

'''
	SOURCES:
		https://www.nasdaq.com/market-activity/stocks/fslr/option-chain
'''


import treasury_weather.stats.aggregate_PC_ratio as aggregate_PC_ratio

def SCAN_JSON_PATH (PATH):
	import json

	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	
	FULL_PATH = normpath (join (FIELD, PATH))
	
	with open (FULL_PATH) as SELECTOR:
		NOTE = json.load (SELECTOR)
	
	return NOTE



def check_1 ():
	EXAMPLE_1 = SCAN_JSON_PATH ("examples/1.JSON")
	EVALUATION = aggregate_PC_ratio.CALC (EXAMPLE_1)
	
	import json
	print ("EVALUATION:", json.dumps (EVALUATION, indent = 4))

	return;
	
	
checks = {
	"check 1": check_1
}