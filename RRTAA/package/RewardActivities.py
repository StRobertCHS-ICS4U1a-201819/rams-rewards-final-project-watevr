class Reward_list(object):
    def __init__(self, reward_list, point_list):
        self.reward_list = reward_list
        self.point_list = point_list

    def get_point_value(self, activities_name):

       for i in range(len(self.reward_list)):
            if activities_name == self.reward_list[i]:
                return self.point_list[i]

reward = Reward_list(["Highest Mark", "Average over 85", "Club Meeting", "Sport Team", "Activities Leader"], [8, 4, 6, 7, 5])