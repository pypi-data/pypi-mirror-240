
'''
	python3 NERVES.py FORMATIONS/STRING/FIND_AND_REPLACE -k test_2
'''

from . import FIND_AND_REPLACE

def test_1 ():
	STRING = FIND_AND_REPLACE ({
		"STRING": "SSSSSZZZZ12341234",
		"FROM": "S",
		"TO": "W"
	})
	
	print (STRING)
	
	assert (STRING == "WWWWWZZZZ12341234")
	
