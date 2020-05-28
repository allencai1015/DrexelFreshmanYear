from maze import Maze
from room import Room

def play(my_maze):
	#Play a game
	while not my_maze.atExit():
		print(my_maze.getCurrent())
		direction = input("Enter direction to move north west east south restart")
		## TODO: Based on choice do what was asked.
		if direction.lower() == "north":
			my_maze.moveNorth()
		elif direction.lower() == "west":
			my_maze.moveWest()
		elif direction.lower() == "east":
			my_maze.moveEast()
		elif direction.lower() == "south":
			my_maze.moveSouth()
		elif direction.lower() == "restart" or direction.lower() == "reset":
			my_maze.reset()
		else:
			print("\nInvalid Entry")
	print("You found the exit!")

# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE
my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dining room?"))
my_rooms.append(Room("This room is the exit. Good Job."))

#room 1 is north of room 0.  Make sure to connect them both ways (it's not a 1-way door!)
my_rooms[0].setEast(my_rooms[1])
my_rooms[1].setWest(my_rooms[0])

#room 2 is east of room 1.  Make sure to connect them both ways (it's not a 1-way door!)
my_rooms[1].setNorth(my_rooms[2])
my_rooms[2].setSouth(my_rooms[1])

SIMPLE_MAZE = Maze(my_rooms[0],my_rooms[2])

# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE
intermediate_rooms = []

intermediate_rooms.append(Room("Room1"))
intermediate_rooms.append(Room("Room2"))
intermediate_rooms.append(Room("Room3"))
intermediate_rooms.append(Room("Room4"))
intermediate_rooms.append(Room("Room5"))
intermediate_rooms.append(Room("Room6"))

#west, west, west, north, east.
intermediate_rooms[0].setWest(intermediate_rooms[1])
intermediate_rooms[1].setEast(intermediate_rooms[0])

intermediate_rooms[1].setWest(intermediate_rooms[2])
intermediate_rooms[2].setEast(intermediate_rooms[1])

intermediate_rooms[2].setWest(intermediate_rooms[3])
intermediate_rooms[3].setEast(intermediate_rooms[2])

intermediate_rooms[3].setNorth(intermediate_rooms[4])
intermediate_rooms[4].setSouth(intermediate_rooms[3])

intermediate_rooms[4].setEast(intermediate_rooms[5])

INTERMEDIATE_MAZE = Maze(intermediate_rooms[0], intermediate_rooms[5])

if __name__=="__main__":
	
	## TODO: Define this play function above and run on your INTERMEDIATE_MAZE
	play(INTERMEDIATE_MAZE)