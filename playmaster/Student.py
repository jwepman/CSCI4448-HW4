#Student.py - implementation of student class
#Josh Wepman, joshua.wepman@colorado.edu
import Instructor

class Student(object):
	name = ""
	weeks = [] #collection of weeks on record for student
	instructor = None #my instructor
	def __init__(self, name, instructor, currentLevel=0):
		self.name = name
		if isinstance(instructor,Instructor.Instructor):
			self.instructor = instructor
		else:
			raise NameError("Invalid instructor specified!")
		self.instructor.addStudent(self)
		self.myCurrentLevel = currentLevel
	def addWeek(self,week):
		self.weeks.append(week)
	def __str__(self):
		myString = "Hi, I'm "+self.name+" (I belong to "+self.instructor.name+") and here is my status:\n"
		for week in self.weeks:
			myString += "--->"
			myString += str(week)
			myString += "\n"
		return myString
	def getCurrentWeekStatus(self):
		return str(weeks[-1])
	def __eq__(self,other):
		return other != None and self.name == other.name