class Student(object):
	"""docstring for Student"""
	def __init__(self, first_name, last_name, id, homeRoom, points):         #name = str; id = int; homeRoom = str; points = int                          
		self.student_firstName = first_name
		self.student_lastName = last_name
		self.student_id = id
		self.student_homeRoom = homeRoom
		self.student_points = int(points)
