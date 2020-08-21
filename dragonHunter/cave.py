# There are the classes and functions for the cave. 

def caveEntrance():
	print("There are 3 ways you can go. l for left")
	print("r for right and f for forward")
	direction = input(">")
	if direction == "r":
		caveR()
	elif direction == "l":
		caveL()
	elif direction == "f":
		caveC()
	else:
		print("computer does not understand")
		
def caveR():
	print("You have been eaten by the dragon.")
	print("Do you want to play again. y or n")
	play = input(">")
	playAgain(play)
def caveL():
	print("You have been eaten by the dragon")
	print("Do you want to play again. y or n")
	play = input(">") 
	playAgain(play)
def caveC():
	print("You have been eaten by the dragon")
	print("Do you want to play again. y or n")
	play = input(">")
	playAgain(play)
def playAgain(p):
	if p == 'y':
		intro()
	elif p == 'n':
		print("Thank you for playing.")

def intro():
	print("Hello welcome to Dragon hunter version 1.0 Beta.")
	print("Press s to start the game")
	s = input(">")
	if s == "s":
		caveEntrance()
	else:
		intro()
		
intro()
	