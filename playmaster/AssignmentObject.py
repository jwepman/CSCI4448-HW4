#AssignmentObject.py - implements assignmentlist object - simply has different default values than parent
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
import PlayObject

class AssignmentObject(PlayObject.PlayObject):
	def __init__(self, playCount=1):
		super(AssignmentObject,self).__init__(playCount)