






'''
	from treasury_weather.tools.ratio import CALC_ratio
'''

def CALC_ratio (S1, S2):
	if (S1 == 0 or S2 == 0):
		#return "CAN'T DIVIDE BY ZERO"
		return [ "~>= INFINITY", 0 ]

	if (S1 == S2):
		return [ 1, 1 ]
	
	elif (S1 >= S2):
		return [
			S1 / S2,
			1
		]
	
	elif (S2 >= S1):
		return [
			1,
			S2 / S1
		]
	
	
	raise ("?")
