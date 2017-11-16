# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Course():
	def __init__(self, name):
		self.name = name
		self.scores = []

	def setScore(self, score):
		self.scores.append(score)

	def getScores(self):
		return self.scores

	def getAverage(self):
		return sum(self.scores)/len(self.scores)

class Diary():
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses = {}

	def setCourse(self, name):
		self.courses[name] = Course(name)

	def setScore(self, courseName, score):
		self.courses[courseName].setScore(score)

	def getCourseAverage(self, course):
		return self.courses[course].getAverage()

	def getTotalAverage(self):
		return sum(course.getAverage() for course in self.courses.values())/len(self.courses)


if __name__=="__main__":
	diary = Diary('Piotr', 'Pabian')
	diary.setCourse('PIPE')
	diary.setCourse('Math')
	diary.setScore('PIPE', 5)
	diary.setScore('PIPE', 2)
	diary.setScore('PIPE', 5)
	diary.setScore('PIPE', 4)
	diary.setScore('Math', 5)
	diary.setScore('Math', 2.5)
	diary.setScore('Math', 4.5)
	diary.setScore('Math', 4.5)
	print diary.getCourseAverage('PIPE')
	print diary.getCourseAverage('Math')
	print diary.getTotalAverage()
