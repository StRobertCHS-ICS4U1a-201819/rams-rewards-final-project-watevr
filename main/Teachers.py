class Teacher(object):
	"""docstring for Teacher"""
	def __init__(self, id, password):            #id = int; password = str      
		self.teacher_id = id
		self.teacher_password = password

	def get_teachers_id(self):
		return self.teacher_id

MrFabroa = Teacher(1, "admin")

	
		