#Mark Boady
#CS 172 - Maze Game
#Drexel University 2018

class Maze:
	#Inputs: Pointer to start room and exit room
	#Sets current to be start room
	def __init__(self,st=None,ex=None):
		pass
		# TODO 
		#Room the player starts in
		self.__st = st
		#If the player finds this room they win
		# TODO
		self.__ex = ex
		#What room is the player currently in
		# TODO
		self.__current = self.__st
		
	#Return the room the player is in (current)
	def getCurrent(self):
		# TODO
		return self.__current

	#The next four all have the same idea
	#See if there is a room in the direction
	#If the direction is None, then it is impossible to go that way
	#in this case return false
	#If the direction is not None, then it is possible to go this way
	#Update current to the new move (move the player)
	#then return true so the main program knows it worked.
	def moveNorth(self):
		cur = self.__current
		if cur.getNorth() is not None:
			self.__current = cur.getNorth()
			print("\nYou went north")
		else :
			print("\nDirection invalid, try again.")

	def moveSouth(self):
		cur = self.__current
		if cur.getSouth() is not None:
			self.__current = cur.getSouth()
			print("\nYou went south")
		else :
			print("\nDirection invalid, try again.")

	def moveEast(self):
		cur = self.__current
		if cur.getEast() is not None:
			self.__current = cur.getEast()
			print("\nYou went east")
		else :
			print("\nDirection invalid, try again.")

	def moveWest(self):
		cur = self.__current
		if cur.getWest() is not None:
			self.__current = cur.getWest()
			print("\nYou went west")
		else :
			print("\nDirection invalid, try again.")

	#If the current room is the exit,
	#then the player won! return true
	#otherwise return false
	def atExit(self):
		# TODO
		if self.__current == self.__ex:
			return True
		else :
			return False

	#If you get stuck in the maze, you should be able to go
	#back to the start
	#This sets current to be the start_room
	def reset(self):
		# TODO
		self.__current = self.__st
		print("\nYou went back to the start!")