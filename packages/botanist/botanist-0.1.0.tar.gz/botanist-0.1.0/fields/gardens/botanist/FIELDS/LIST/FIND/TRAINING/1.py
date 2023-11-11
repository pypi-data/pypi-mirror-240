

LIST_2 = [{
	"NUMBER": 1
},{
	"NUMBER": 9
},{
	"NUMBER": 3
},{
	"NUMBER": 0
},{
	"NUMBER": 8
}]

def GET_ENTRY (LIST):
	for ENTRY in LIST:
		if (ENTRY["NUMBER"] == 9):
			return ENTRY;

ENTRY = lambda ENTRY : ENTRY 

ENTRY = GET_ENTRY (LIST_2)
ENTRY["NUMBER"] = 11

print (ENTRY)
