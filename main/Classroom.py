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

	def add_teacher(self, teacher):               #这个真的需要吗？
		self.teacher_list.append(teacher)

	def remove_student(self, student, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_newList.remove(student)


	def edit_student_info(self, student, first_name, last_name, id, homeRoom, points):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_firstName = first_name
				self.student_lastName = last_name
				self.student_id = id
				self.student_homeRoom = homeRoom
				self.student_points = int(points)

	def edit_student_firstname(self, student, first_name, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_firstName = first_name


	def edit_student_lastname(self, student, last_name, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_lastName = last_name


	def edit_student_id(self, student, new_id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_id = new_id

	def edit_student_hoomRoom(self, student, hoomRoom, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_hoomRoom = hoomRoom

	def edit_student_point(self, student, points, id):
		for sid in self.student_newList:
			if sid == student_id:
				self.student_points = points









		
		