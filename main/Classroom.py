import Students
import Teachers


class Classroom(object):
	"""docstring for Classroom"""
	def __init__(self):
		self.student_list = []
		self.teacher_list = []
	
	def add_student(self, student):
		self.student_list.append(student)

	def add_teacher(self, teacher):
		self.teacher_list.append(teacher)


		
		