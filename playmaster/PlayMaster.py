#PlayMaster.py - abstract the basics from our simulator
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
from PersistenceHandler import *
class PlayMaster(object):
	__persistenceHandler = None
	__objectsDictionary = None
	def __init__(self):
		self.__persistenceHandler = PersistenceHandler()
		self.__objectsDictionary = self.__persistenceHandler.getCurrentDict()
		for s in self.__objectsDictionary['students']:
			s.weeks.append(self.__objectsDictionary['weeks'][0])
			
			
	def getByName(self,key,name):
		try:
			for student in self.__objectsDictionary[key]:
				if student.name == name:
					return student
		except KeyError:
			self.__objectsDictionary[key] = set()
		print "Bzzzt! Object not found in persistence object!"
		return None
	def addByName(self,key,element):
		try:
			self.__objectsDictionary[key].add(element)
		except KeyError:
			self.__objectsDictionary[key] = set()
			self.__objectsDictionary[key].add(element)
		self.__updatePersistenceObj()
	def getCurrentKeyList(self,key):
		#return a list of current {key}->name
		retList = []
		try:
			for element in self.__objectsDictionary[key]:
				retList.append(element.name)
		except KeyError:
			pass
		return retList
				
	def __updatePersistenceObj(self):
		self.__persistenceHandler.setCurrentDict(self.__objectsDictionary)
		self.__persistenceHandler.write()
	def __del__(self):
		#backup - save our state!
		self.__updatePersistenceObj() 
		