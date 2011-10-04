#Instructor.py - implements instructor class for my music thingy
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
import Student

class Instructor(object):
	students = set() #1:many mapping of instructors:students
	name = ""
	def __init__(self,name):
		self.name = name
		self.students = set()
	def addStudent(self,student):
		if isinstance(student,Student.Student):
			self.students.add(student)
		else:
			print "Bzzzt! You can't fool me -- that's not a student"
	def removeStudent(self,student):
		try:
			self.students.remove(student)
		except KeyError:
			print "Bzzzt! Student does not exist in list!"
	def __str__(self):
		myString = "Hello, I'm "+self.name+" (instructor, so don't mess with me) and here are my students (if any):\n"
		for student in self.students:
			myString += "->"+str(student)+"\n"
		return myString
	def __eq__(self,other):
		return other != None and self.name == other.name