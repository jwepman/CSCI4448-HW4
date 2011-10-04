#PersistenceHandler.py - handle persistence for this project - we serialize all of our objects and store in a massive JSON-esque dictionary that we pass to PlayMaster
#Josh Wepman, joshua.wepman@colorado.edu
import pickle #for serialization
import os

class PersistenceHandler(object):
	__currentDict = {}
	persistenceFileName = "./database/persist.json"
	__state = 1 #0 for unserialized, 1 for serialized
	def __init__(self,overRideFileName=None):
		if overRideFileName != None:
			self.persistenceFileName = overRideFileName
		self.read()
	def getCurrentDict(self):
		if self.__state==1:
			self.__deserialize()
		return self.__currentDict
	def setCurrentDict(self,dictionary):
		self.__state=0
		self.__currentDict = dictionary
		self.__serialize()
	def read(self):
		#read in persistence file, if exists. Returns dictionary of lists of objects, keyed by object type.
		if os.path.exists(self.persistenceFileName):
			myFile = open(self.persistenceFileName, "r")
			mySerializedText = myFile.read()
			myFile.close()
		else:
			self.__currentDict = {}
			return self.__currentDict
		#now, iterate through returned object and de-serialize it
		if mySerializedText == "":
			self.__currentDict = {}
			return self.__currentDict
		self.__state = 1
		self.__currentDict = mySerializedText
		self.__deserialize()
		return self.__currentDict
	def write(self):
		#write __currentDict to file, to persist ~~ do encoding in JSON first
		self.__serialize()
		mySerializedText = self.__currentDict
		myFile = open(self.persistenceFileName,"w")
		myFile.write(mySerializedText)
		myFile.close()
	def clearPersistenceFile(self):
		print "Really clear persistence file? [y/n]"
		x = raw_input()
		if x.capitalize() == 'Y':
			self.__currentDict = {}
			myFile = open(self.persistenceFileName,"w")
			myFile.write("")
			myFile.close()
		else:
			print "aborting clear operation user said: "+x
	def __toggleSerialization(self):
		#serialize/deserialize my object based on state variable
		if self.__state==0:
			self.__serialize()
		else:
			self.__deserialize()
	def __serialize(self):
		if self.__state==1:
			#already serialized
			return
		self.__currentDict = pickle.dumps(self.__currentDict)
		self.__state=1
	def __deserialize(self):
		if self.__state==0:
			#already deserialized
			return
		self.__currentDict = pickle.loads(self.__currentDict)
		self.__state=0