


'''
	This checks if a partial string
	is at the end of another string.
'''
def END_OF_STRING_IS (STRING, PARTIAL):
	try:
		INDEX = STRING.index (PARTIAL)

		if (len (STRING) == (INDEX + len (PARTIAL)):
			return True
	except Exception:
		pass

	return False