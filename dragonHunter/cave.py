# There are the classes and functions for the cave. 

# none -> string
# output what happens in room one
# def roomOne()
def roomOne():
	print("You are now in room one. The dragon is in the room. Now you need to capture the dragon.")
	print("1 lunge at the dragon")
	print("2 attempt to talk the dragon and take him peacefully.")
	print("3 Tell the dragon a joke to catch him off gard and arrest him.")
	print("4 challenge him to a fight.")
	choice = input("<")
	if choice == "1":
		print("The dragon blocks you. You are dead game over.")
	elif choice == "2" :
		print("All talk and no action makes for a dead dragon humter.")
	elif choice == "3":
		print("Dragons have no sense of hunor. You are dead game over.")
	elif choice == "4":
		print("You have no chance. BUt, you win anyway and capture the dragon. You win.")

roomOne()