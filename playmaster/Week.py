#Week.py - week class handles keeping track of week data for a student
# Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
import datetime
import PlayObject

class Week(object):
	myPlayList = set([]) #set of play objects to play
	weekStartDate = None #this is a start date for the week, lasting seven days inclusive
	level=0
	def __init__(self,startDate=datetime.date.today(),level=0):
		self.weekStartDate = startDate
		self.level=level
		self.myPlayList = set()
	def addPlayItem(self,playItem):
		if isinstance(playItem,PlayObject.PlayObject):
			self.myPlayList.add(playItem)
		else:
			print "Bzzzt! You can't add that item, it's not a playable object!"
	def playAllSongs(self):
		for element in self.myPlayList:
			element.playSong()
	def playOneSong(self, song):
		for element in self.myPlayList:
			if song == element.song:
				element.playSong
	def __copy__(self):
		#copy week to new one (basically increments level and copies previous play lists correctly)
		result = Week(datetime.date.today(),self.level+1)
		for element in self.myPlayList:
			result.addPlayItem(element.copy())
		return result
	def __str__(self):
		result = "Week "+str(self.weekStartDate)+" has the following songs: \n"
		for song in self.myPlayList:
				result += "------>"+str(song)+"\n"
		return result