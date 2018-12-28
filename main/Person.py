class Person(object):
	"""docstring for Person"""
	def __init__(self, first_name, last_name, ID, hoomRoom, points = 0):
		self.first_name = first_name
		self.last_name = last_name
		self.person_id = ID
		self.person_homeRoom = hoomRoom
		self.person_points = points

	def edit_person_info(self, first_name, last_name, homeRoom, points):
		person_id = input("Please input ID: ")
		for ID in self.person_newList:
			if ID.person_id == person_id:
				self.person_firstName = first_name
				self.person_lastName = last_name
				self.person_id = id
				self.person_homeRoom = homeRoom
				self.person_points = int(points)

	def edit_person_firstname(self, person, first_name, person_id):
		for ID in self.person_newList:
			if ID.person_id == person_id:
				self.person_firstName = first_name


	def edit_person_lastname(self, person, last_name, id):
		for sid in self.person_newList:
			if sid == person_id:
				self.person_lastName = last_name


	def edit_person_id(self, person, new_id):
		for sid in self.person_newList:
			if sid == person_id:
				self.person_id = new_id

	def edit_person_hoomRoom(self, person, hoomRoom, id):
		for sid in self.person_newList:
			if sid == person_id:
				self.person_hoomRoom = hoomRoom

	def edit_person_point(self, person, points, id):
		for sid in self.person_newList:
			if sid == person_id:
				self.person_points = points