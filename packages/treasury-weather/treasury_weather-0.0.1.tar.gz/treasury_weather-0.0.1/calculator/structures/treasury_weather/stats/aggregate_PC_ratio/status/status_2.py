

'''
	python3 STATUS.py "/stats/aggregate_PC_ratio/STATUS/STATUS_2.py"
'''

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



def CHECK_1 ():
	EXAMPLE = SCAN_JSON_PATH ("examples/2.JSON")
	EVALUATION = aggregate_PC_ratio.CALC (EXAMPLE)
	
	import json
	print ("EVALUATION:", json.dumps (EVALUATION, indent = 4))

	assert (EVALUATION ["expirations"][0]["SUMS"]["PUTS"]["ask"] == 2000)
	assert (EVALUATION ["expirations"][0]["SUMS"]["PUTS"]["bid"] == 1200)
	assert (EVALUATION ["expirations"][0]["SUMS"]["PUTS"]["last"] == 0)

	assert (EVALUATION ["expirations"][0]["SUMS"]["calls"]["ask"] == 2000)
	assert (EVALUATION ["expirations"][0]["SUMS"]["calls"]["bid"] == 1700)
	assert (EVALUATION ["expirations"][0]["SUMS"]["calls"]["last"] == 3600)

	assert (EVALUATION ["expirations"][0]["PC ratios"]["ask"] == [ 1, 1 ])
	assert (EVALUATION ["expirations"][0]["PC ratios"]["bid"] == [ 1, 1.4166666666666667 ])
	assert (EVALUATION ["expirations"][0]["PC ratios"]["last"] == [ "~>= INFINITY", 0 ])

	assert (EVALUATION ["PC ratios"]["ask"] == [ 1, 1 ])
	assert (EVALUATION ["PC ratios"]["bid"] == [ 1, 1.4166666666666667 ])
	assert (EVALUATION ["PC ratios"]["last"] == [ "~>= INFINITY", 0 ])

	assert (EVALUATION ["SUMS"]["PUTS"]["ask"] == 2000)
	assert (EVALUATION ["SUMS"]["PUTS"]["bid"] == 1200)
	assert (EVALUATION ["SUMS"]["PUTS"]["last"] == 0)

	assert (EVALUATION ["SUMS"]["calls"]["ask"] == 2000)
	assert (EVALUATION ["SUMS"]["calls"]["bid"] == 1700)
	assert (EVALUATION ["SUMS"]["calls"]["last"] == 3600)

	return;
	
	
checks = {
	"CHECK 1": CHECK_1
}