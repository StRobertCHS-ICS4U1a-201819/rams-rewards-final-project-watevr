class Teacher(object):
	"""docstring for Teacher"""
	def __init__(self, first_name, last_name, ID, password):          #id = int; password = str      
		self.teacher_fistName = first_name
		self.teacher_lastName = last_name
		self.teacher_id = ID
		self.teacher_password = password

	def get_teachers_id(self):
		return self.teacher_id

MrFabroa = Teacher(1, "admin")

