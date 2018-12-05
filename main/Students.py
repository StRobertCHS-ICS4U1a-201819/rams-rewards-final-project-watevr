class Student(object):
	"""docstring for Student"""
	def __init__(self, name, id, homeRoom, points = 0):         #name = str; id = int; homeRoom = str                              
		self.student_name = name
		self.student_id = id
		self.student_homeRoom = homeRoom
		self.student_points = points

justin = Student("justin", 2, "cs")
evan = Student("evan", 1, "cs")
jerry = Student("jerry", 3, "cs")
warden = Student("jerry", 4, "cs")
alvin = Student("alvin", 5, "cs")
