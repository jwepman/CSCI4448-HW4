#_populateWeeks.py

import datetime, Week,PersistenceHandler, PlayListObject, Week, Student, Song, PlayListObject, Instructor
ph = PersistenceHandler.PersistenceHandler()
d = {}

songs = set([])
songs.add(Song.Song("Ima Beginner",0))
songs.add(Song.Song("Hot Cross Buns",0))
songs.add(Song.Song("Practice Scale 1",0))
songs.add(Song.Song("Twinkle, Twinkle",1))
songs.add(Song.Song("Baa Baa Black Sheep",1))
songs.add(Song.Song("Practice Scale 2",1))
songs.add(Song.Song("Fur Elise",2))
songs.add(Song.Song("Practice Scale 3",2))
songs.add(Song.Song("Raspberry in Azure",3))
songs.add(Song.Song("Chopsticks",3))
songs.add(Song.Song("Practice Scale 1",3))
songs.add(Song.Song("Bach Schmettrling",4))
songs.add(Song.Song("The Entertainer",4))
songs.add(Song.Song("Tiger Rag",4))
songs.add(Song.Song("Practice Chord 2",4))
songs.add(Song.Song("Practice Chord 3",5))
songs.add(Song.Song("Clocks",5))

instructors = []
instructors.append(Instructor.Instructor("Donald Duck"))
instructors.append(Instructor.Instructor("Jose Carioca"))
instructors.append(Instructor.Instructor("Panchito"))

students = []
students.append(Student.Student("Goofy",instructors[2]))
students.append(Student.Student("Daisy Duck",instructors[0]))
students.append(Student.Student("Micky Mouse",instructors[1]))
students.append(Student.Student("Minnie Mouse",instructors[1]))

for stu in students:
	for level in range(5):
		week = Week.Week(datetime.date(2011,9,(level*7)+1),level)
		for song in songs:
			if song.level == level:
				myPlayItem = PlayListObject.PlayListObject()
				myPlayItem.assignSong(song)
				week.addPlayItem(myPlayItem)
		stu.weeks.append(week)

d = {
	'students': students,
	'songs': songs,
	'instructors': instructors
	}
	
ph.setCurrentDict(d)
ph.write()