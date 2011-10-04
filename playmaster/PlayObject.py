#PlayObject.py - parent class for PlayList and AssignmentList -- provides general specification for these objects to implement
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
import datetime

class PlayObject(object):
	song = None #corresponding song
	requiredPlayCount = 1
	currentPlayCount = 0
	lastPlayed = None
	def __init__(self,playCount=1):
		self.requiredPlayCount = playCount
	def assignSong(self,song):
		self.song = song
	def playSong(self):
		if (self.requiredPlayCount-self.currentPlayCount) <= 0:
			print "You are an overachiever, you've already played this song too many times!"
		self.currentPlayCount += 1
		self.lastPlayed = datetime.datetime.now()
	def resetPlayCount(self):
		self.currentPlayCount = 0
	def __copy__(self):
		#make copy and return with zero play count
		result = PlayObject(self.requiredPlayCount)
		result.song = self.song
		result.currentPlayCount = 0
		return result
	def __str__(self):
		return "PlayObject<"+str(self.song)+"> play count="+str(self.currentPlayCount)+" out of "+str(self.requiredPlayCount)+" lastplayed on: "+str(self.lastPlayed)
	def __eq__(self,other):
		#comparison of play objects -- by song
		return self.song == other.song