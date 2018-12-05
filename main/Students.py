class Student(object):
	"""docstring for Student"""
	def __init__(self, name, id, homeRoom, points = 0):
		self.student_name = name
		self.student_id = id
		self.student_homeRoom = homeRoom
		self.student_points = points

justin = Student("justin", 123, "cs")