class Student(object):
	"""docstring for Student"""
	def __init__(self, name, id, homeRoom, points):         #name = str; id = int; homeRoom = str; points = int
		self.student_name = name
		self.student_id = id
		self.student_homeRoom = homeRoom
		self.student_points = points

	def get_Name(self):
		return self.student_name

justin = Student("justin", 2, "cs", 0)
evan = Student("evan", 1, "cs", 0)
jerry = Student("jerry", 3, "cs", 0)
warden = Student("jerry", 4, "cs", 0)
alvin = Student("alvin", 5, "cs", 0)
