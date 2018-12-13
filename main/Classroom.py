from main import Teachers
from main import Students



class Classroom(Students):
	"""docstring for Classroom"""
	def __init__(self):
		super().__init__()      #get class "student"

		self.student_list = []
		self.teacher_list = []
	
	def __get_student(self):
		for lst in self.student_newList:
			self.student_list.append(Students(s for s in self.student_newList))

	def add_student(self, student):
		self.student_list.append(student)

	def add_teacher(self, teacher):               #这个真的需要吗？
		self.teacher_list.append(teacher)

	def remove_student(self, student, id):
		for sid in self.student_newList:
			if sid == self.student_id:
				self.student_newList.remove(student)

