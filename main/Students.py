class Student(object):
	"""docstring for Student"""

    def __init__(self, first_name, last_name, ID, homeRoom, points):         #name = str; id = int; homeRoom = str; points = int
        self.student_firstName = first_name
        self.student_lastName = last_name
        self.student_id = ID
        self.student_homeRoom = homeRoom
        self.student_points = int(points)

    def get_Name(self):
        return self.student_name

	def edit_person_info(self, first_name, last_name, ID, homeRoom, points):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.person_firstName = first_name
				self.person_lastName = last_name
				self.student_id = ID
				self.person_homeRoom = homeRoom
				self.person_points = int(points)

	def edit_person_firstname(self, person, first_name):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.person_firstName = first_name


	def edit_person_lastname(self, person, last_name, id):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.person_lastName = last_name


	def edit_person_id(self, person, new_id):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.student_id = new_id

	def edit_person_hoomRoom(self, person, hoomRoom, id):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.person_hoomRoom = hoomRoom

	def edit_person_point(self, person, points, id):
		student_ID = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.student_id == student_ID:
				self.person_points = points
