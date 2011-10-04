#PlayListObject.py - implements playlist object - simply has different default values
#Josh Wepman, joshua.wepman@colorado.edu and Kyle Poole, 2kylepoole@gmail.com
import PlayObject

class PlayListObject(PlayObject.PlayObject):
	def __init__(self, playCount=5):
		super(PlayListObject,self).__init__(playCount)