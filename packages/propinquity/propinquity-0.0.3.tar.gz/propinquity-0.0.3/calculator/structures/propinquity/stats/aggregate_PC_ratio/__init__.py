
'''
	import propinquity.stats.aggregate_PC_ratio as aggregate_PC_ratio
	EVALUATION = aggregate_PC_ratio.CALC (EXAMPLE_1)
	
	import json
	print ("EVALUATION:", json.dumps (EVALUATION, indent = 4))
'''

'''
	OUTPUT:
	
	{
		"expirations": [{
			"expiration": "2023-10-27",
			"SUMS": {
				"PUTS": {
					"ask":
					"bid":
					"last"
				},
				"calls": {
					"ask":
					"bid":
					"last"
				}
			},
			"PC ratios": {
				"ask":
				"bid":
				"last"
			}
		}],
		"SUMS": {
			"PUTS": {
				"ask":
				"bid":
				"last"
			},
			"calls": {
				"ask":
				"bid":
				"last"
			}
		},
		"PC ratios": {
			"ask":
			"bid":
			"last"
		}
	}
'''

from propinquity.tools.ratio import CALC_ratio

import pydash
def RETURN_NUMBER (OBJECT, PATH, DEFAULT):
	FOUND = pydash.get (
		OBJECT,
		PATH,
		DEFAULT
	)
	
	TYPE = type (FOUND)
	if (TYPE == int or TYPE == float):
		return FOUND
		
	if (FOUND == None):
		return DEFAULT;

	print ("FOUND WAS NOT ACCOUNTED FOR:", FOUND)
	raise Exception (f"FOUND WAS NOT ACCOUNTED FOR: { FOUND }")
		
	return DEFAULT

def RETRIEVE_MULTIPLICAND (strike):
	return strike ["contract size"] * strike ["open interest"]
 
	try:
		pass;
	
	except Exception as E:
		pass;
		

def EQUALITY_CHECK (PARAM_1, PARAM_2):
	try:
		assert (PARAM_1 == PARAM_2)
	except Exception as E:
		import traceback
		
		print ("PARAM 1", PARAM_1)
		print ("PARAM 2", PARAM_2)	
		
		print (traceback.print_exception (E))

		raise Exception (E)

	return
	

def CALC (CHAIN):
	expirations = CHAIN ["expirations"]
	
	EVALUATION = {
		"expirations": [],
		"SUMS": {
			"PUTS": {
				"ask": 0,
				"bid": 0,
				"last": 0
			},
			"calls": {
				"ask": 0,
				"bid": 0,
				"last": 0
			}
		},
		"PC ratios": {
			"ask": 0,
			"bid": 0,
			"last": 0
		}
	}
	
	
	for expiration in expirations:
		calls_strikes = expiration ["calls"]["strikes"]
		PUTS_strikes = expiration ["PUTS"]["strikes"]
		
		expiration_NOTE = {
			"expiration": expiration ["expiration"],
			"SUMS": {
				"PUTS": {
					"ask": 0,
					"bid": 0,
					"last": 0
				},
				"calls": {
					"ask": 0,
					"bid": 0,
					"last": 0
				}
			},
			"PC ratios": {
				"ask": 0,
				"bid": 0,
				"last": 0
			}
		}
		
		EQUALITY_CHECK (len (calls_strikes), len (PUTS_strikes))
		
		DIRECTION = "calls"
		for strike in calls_strikes:		
			expiration_NOTE ["SUMS"][ DIRECTION ]["ask"] += RETURN_NUMBER (strike, [ "prices", "ask" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["SUMS"][ DIRECTION ]["bid"] += RETURN_NUMBER (strike, [ "prices", "bid" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["SUMS"][ DIRECTION ]["last"] += RETURN_NUMBER (strike, [ "prices", "last" ], 0) * RETRIEVE_MULTIPLICAND (strike)
		
		DIRECTION = "PUTS"
		for strike in PUTS_strikes:		
			expiration_NOTE ["SUMS"][ DIRECTION ]["ask"] += RETURN_NUMBER (strike, [ "prices", "ask" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["SUMS"][ DIRECTION ]["bid"] += RETURN_NUMBER (strike, [ "prices", "bid" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["SUMS"][ DIRECTION ]["last"] += RETURN_NUMBER (strike, [ "prices", "last" ], 0) * RETRIEVE_MULTIPLICAND (strike)
		
		expiration_NOTE ["PC ratios"]["ask"] = CALC_ratio (
			expiration_NOTE ["SUMS"][ "PUTS" ]["ask"],
			expiration_NOTE ["SUMS"][ "calls" ]["ask"]
		)
		expiration_NOTE ["PC ratios"]["bid"] = CALC_ratio (
			expiration_NOTE ["SUMS"][ "PUTS" ]["bid"],
			expiration_NOTE ["SUMS"][ "calls" ]["bid"]
		)
		expiration_NOTE ["PC ratios"]["last"] = CALC_ratio (
			expiration_NOTE ["SUMS"][ "PUTS" ]["last"],
			expiration_NOTE ["SUMS"][ "calls" ]["last"]
		)
		
		EVALUATION ["SUMS"][ "calls" ]["ask"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "calls", "ask" ], 0)
		EVALUATION ["SUMS"][ "calls" ]["bid"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "calls", "bid" ], 0)
		EVALUATION ["SUMS"][ "calls" ]["last"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "calls", "last" ], 0)
		
		EVALUATION ["SUMS"][ "PUTS" ]["ask"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "PUTS", "ask" ], 0)
		EVALUATION ["SUMS"][ "PUTS" ]["bid"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "PUTS", "bid" ], 0)
		EVALUATION ["SUMS"][ "PUTS" ]["last"] += RETURN_NUMBER (expiration_NOTE, [ "SUMS", "PUTS", "last" ], 0)
		
		EVALUATION ["expirations"].append (expiration_NOTE)
		
	EVALUATION ["PC ratios"]["ask"] = CALC_ratio (
		EVALUATION ["SUMS"][ "PUTS" ]["ask"],
		EVALUATION ["SUMS"][ "calls" ]["ask"]
	)
	
	EVALUATION ["PC ratios"]["bid"] = CALC_ratio (
		EVALUATION ["SUMS"][ "PUTS" ]["bid"],
		EVALUATION ["SUMS"][ "calls" ]["bid"]
	)
	
	EVALUATION ["PC ratios"]["last"] = CALC_ratio (
		EVALUATION ["SUMS"][ "PUTS" ]["last"],
		EVALUATION ["SUMS"][ "calls" ]["last"]
	)

	return EVALUATION