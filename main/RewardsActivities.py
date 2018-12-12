class Reward(object):
    def __init__(self, activities, point_value):
        self.activities = activities
        self.point_value = point_value

    def get_point_value(self):
        return self.point_value


reward1 = Reward("Highest Mark", 8)
reward2 = Reward("Average over 85", 4)
reward3 = Reward("Club Meeting", 5)
reward4 = Reward("Sport Team", 7)
reward5 = Reward("Activities Leader", 9)