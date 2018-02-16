print "Welcome to UsoroOS Test Sync App"
choice = raw_input ('Do you want to (S)end or (R)ecieve?')
sendChoice = ['s', 'send']
recieveChoice = ['r', 'recieve']

def ChoiceFunction()
if choice in sendChoice:
		import usoroserver
	if choice in recieveChoice: 
		import usoroclient
	else:
		print "Invalid input, exiting"
		exit (1)

c=ChoiceFunction()

