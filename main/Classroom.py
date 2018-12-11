import Students
import Teachers

student_file = open('Students.txt', 'r+')
teacher_file = open('Teachers.txt', 'r+')
studentList = student_file.readlines()
teacherList = teacher_list.readlines()
student_newList = []

for lst in studentList:
	student_newList.append(lst.split(","))

for lst in teacherList:
	teacher_newList.append(lst.split(","))

class Classroom(object):
	"""docstring for Classroom"""
	def __init__(self):
		self.student_list = []
		self.teacher_list = []
	
	def __get_student(self):
		for lst in student_newList:
			self.student_list.append(Students(s for s in student_newList))

	def add_student(self, student):
		self.student_list.append(student)

	def add_teacher(self, teacher):
		self.teacher_list.append(teacher)



		
		