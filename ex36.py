from sys import exit

def dead_room():
	"This room is dead room, if you are here, you are can to sal some with one opcion, your choose de correct ask"
	print "Choose the option correct for to salve your life"
	print "Option 1 : wooden knives"
	print "Option 2 : AR15"
	print "Option 3 : poisonous weed"
	print "Remember, choose one opcion make no mistake"
	
	option = raw_input("> ")
	

	if "1" in option or "2" in option or "3" in option:
		value = int(option)
	else:
		limbo_room("Do you lost in limbo")

	if value <= 3 and value >0:
		if value == 1:
			salved("You are salved, good bye")
		elif value == 2:
			dead("You are dead, good by")
		else:
			oportunity("You are other oportunity")
	else:
		limbo_room("Do you lost un limbo")

	
	
def limbo_room(text):
	print text
	print "You have one oportunity for to get out here"
	print "Option 1: I don't to go here"
	print "Option 2: I walk forever"
	print "Option 3: I have hope"
	
	option = raw_input("> ")
	
	if "1" in option or "2" in option or "3" in option:
		value = int(option)
	else:
		dead("You have dead")
	
	if value == 1:
		dead("You have dead for you")
	elif value == 2:
		dead("You have walk lost forever")
	else:
		dead_room()

def salved(text):
	print text
	exit(0)

def dead(text):
	print text
	exit(0)

def oportunity(text):
	print text
	dead_room()


def start():
	print "Choise one option:"
	print "1-->Enter in the game"

	option = raw_input("> ")

	if "1" in option:
		dead_room()
	else:
		limbo_room("You are lost")

start()
