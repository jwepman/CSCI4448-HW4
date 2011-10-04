#PlayMasterSimulator.py -- graphical interface to our playlist system!
#Yes, there's a lot of strings/code and stuff -- this is for the simulation, each option interacts with the applicable objects and the PlayMaster by passing appropriate messages to each object.
#Josh Wepman, joshua.wepman@colorado.edu
from PlayMaster import *
from Song import * 
from Student import *
from PlayListObject import *
from AssignmentObject import *
from Instructor import *
from Week import * 

class PlayMasterSimulator(object):
	__playMaster = None
	def __init__(self):
		self.__playMaster = PlayMaster()
	def haveFun(self):
		#do our shit here
		for i in range(100):
			print "\n"
		print "Welcome to the PlayMaster 1990 Simulator (feels like 1990, doesn't it?)"
		print "These are the current students in the system:"
		print str(self.__playMaster.getCurrentKeyList('students'))
		print "These are the current instructors in the system:"
		print str(self.__playMaster.getCurrentKeyList('instructors'))
		print "These are the current songs in the system:"
		print str(self.__playMaster.getCurrentKeyList('songs'))
		print "Main Menu:"
		print "1) Add Song to Library"
		print "2) Add Student"
		print "3) Add Instructor"
		print "4) Assign Song to Student"
		print "5) Mark Song Played for Student"
		print "6) Mark All Current Songs Played for Student"
		print "7) Print Current Weekly Report for Student"
		print "8) Print Current Monthly Report for Student"
		print "0) EXIT PROGRAM"
		myInp = input()
		if myInp == 0:
			return -1
		elif myInp == 1:
			print "\n\n"
			print "Enter the name of the song:"
			name = raw_input()
			print "Enter the level of the song 1-5"
			level = input()
			newSong = Song(name,level)
			self.__playMaster.addByName('songs',newSong)
			self.doEnterContinue()
		elif myInp == 2:
			print "\n\n"
			print "Enter the name of the student:"
			myName = raw_input()
			print "Enter the name of the instructor"
			insName = raw_input()
			myInstructor = self.__playMaster.getByName('instructors',insName)
			if myInstructor == None:
				return
			newStudent = Student.Student(myName,myInstructor)
			self.__playMaster.addByName('students',newStudent)
			self.doEnterContinue()
		elif myInp == 3:
			print "\n\n"
			print "Enter the name of the instructor"
			insName = raw_input()
			newIns = Instructor(insName)
			self.__playMaster.addByName('instructors',newIns)
			self.doEnterContinue()
		elif myInp == 4:
			pass
		elif myInp == 5:
			pass
		elif myInp == 6:
			print "\n\n"
			print "Enter student name?"
			name = raw_input()
			myStudent = self.__playMaster.getByName('students',name)
			if myStudent != None and len(myStudent.weeks) > 0:
				myStudent.weeks[-1].playAllSongs()
			self.doEnterContinue()
		elif myInp == 7:
			print "\n\n"
			print "Enter student name?"
			name = raw_input()
			myStudent = self.__playMaster.getByName('students',name)
			if myStudent != None and len(myStudent.weeks) >0:
				print myStudent.weeks[-1]
			else:
				print "{No Week Data Exist!}"
			self.doEnterContinue()
		elif myInp == 8:
			print "\n\n"
			print "Enter student name?"
			name = raw_input()
			myStudent = self.__playMaster.getByName('students',name)
			print myStudent
			self.doEnterContinue()
		else:
			pass
	def doEnterContinue(self):
		print "Press <ENTER> to continue!"
		dum = raw_input()
		return


#####################
# Main Program
mySimObj = PlayMasterSimulator()
returnCode = 0
while returnCode != -1:
	#loop until user terminates program :)
	returnCode = mySimObj.haveFun()

