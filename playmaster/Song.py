#Song.py - implements song class 
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
class Song(object):
	name = ""
	level = 0
	def __init__(self, name, level=0):
		self.name = name
		self.level = level
	def __str__(self):
		return self.name+" <"+str(self.level)+">"
	def __eq__(self, other):
		return other != None and self.name == other.name and self.level == other.level