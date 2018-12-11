import Students
import Teachers

student_file = open('Students.txt', 'r+')
teacher_file = open('Teachers.txt', 'r+')
studentList = student_file.readlines()
teacherList = teacher_list.readlines()
student_newList = []
teacher_newList = []

for lst in studentList:
	student_newList.append(lst.split(","))

for lst in teacherList:
	teacher_newList.append(lst.split(","))

class Classroom(Student):
	"""docstring for Classroom"""
	def __init__(self):
		super().__init__()      #get class "student"

		self.student_list = []
		self.teacher_list = []
	
	def __get_student(self):
		for lst in student_newList:
			self.student_list.append(Students(s for s in student_newList))

	def add_student(self, student):
		self.student_list.append(student)

	def add_teacher(self, teacher):               #这个真的需要吗？
		self.teacher_list.append(teacher)

	def remove_student(self, student, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_newList.remove(student)