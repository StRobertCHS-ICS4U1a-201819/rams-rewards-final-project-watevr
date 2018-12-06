import Classroom

class Reward(object):
	"""docstring for Reward"""
	def __init__(self, activity, point):         #activity = str; point = int
		super(Reward, self, point).__init__()
		self.activity = activity
        self.point = point