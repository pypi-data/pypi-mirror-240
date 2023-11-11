

'''
	from PYTAYA.FORMATIONS.STRING.FIND_AND_REPLACE import FIND_AND_REPLACE
'''

'''
	STRING = FIND_AND_REPLACE ({
		"STRING": "START ZZZZ START 12341234",
		"FROM": "START",
		"TO": "RUN"
	})
'''


def		FIND_AND_REPLACE	(ASK):

	FROM 	= ASK ["FROM"]
	TO 		= ASK ["TO"]
	
	STRING	= ASK ["STRING"]
	
	if ("INFO" in ASK):
		INFO	= ASK ["INFO"]
	else:
		INFO = 0;
	
	FOUND = []
	FROM_INDEX = 0
	FROM_LAST_INDEX = len (FROM) - 1
	FROM_NEXT_CHARACTER = FROM [ FROM_INDEX ]
	
	TO_ADD = []
	
	def REFRESH ():
		print ("REFRESHING")

		nonlocal FOUND
		nonlocal FROM_INDEX
		nonlocal FROM_LAST_INDEX
		nonlocal FROM_NEXT_CHARACTER
		
		FOUND = []
		FROM_INDEX = 0
		FROM_LAST_INDEX = len (FROM) - 1
		FROM_NEXT_CHARACTER = FROM [ FROM_INDEX ]

	FRESH = []
	for CHARACTER in STRING:
		if (INFO >= 1):
			print ("CHARACTER:", CHARACTER)
			print (CHARACTER, FOUND, FROM_INDEX, FROM_LAST_INDEX)
			print ()

		if (CHARACTER == FROM_NEXT_CHARACTER):
			FOUND.append (CHARACTER)
				
			if (FROM_INDEX == FROM_LAST_INDEX):
				#
				#	FROM STRING FOUND!
				#
				
				print ("FROM STRING FOUND!")
				
				FRESH += TO
				
				REFRESH ()
				
			else:
				FROM_INDEX += 1
				FROM_NEXT_CHARACTER = FROM [ FROM_INDEX ]
			
		else:
			FRESH += FOUND
		
			REFRESH ()
		
			FRESH.append (CHARACTER)
		
	
	FRESH += FOUND
			

	return "".join (FRESH)