class Student(object):
    def __init__(self, fName, lName, id, point, reward_history_list):
        self.fName = fName
        self.lName = lName
        self.id = id
        self.point = point
        self.reward_history_list = reward_history_list

    def get_fullName(self):
        return self.fName + self.lName

    def add_point(self, value):
        self.point += value
        return self.point

    def add_reward_history_list(self, activities):
        self.reward_history_list.append(activities)

class Student_list(object):
    def __init__(self, student_list):
        self.student_list = student_list

    def add_student(self, new_student):
        self.student_list.append(new_student)



    def get_student_object(self, id):
        id_list = id.split()
        for i in range(len(id_list)):

            id_value = int(id_list[i])
            if id_value == 1:
                student1.add_point(reward_info.point_reward)
                student1.add_reward_history_list(reward_info.activities)

            elif id_value == 2:
                student2.add_point(reward_info.point_reward)
                student2.add_reward_history_list(reward_info.activities)


            elif id_value == 3:
                student3.add_point(reward_info.point_reward)
                student3.add_reward_history_list(reward_info.activities)


            elif id_value == 4:
                student4.add_point(reward_info.point_reward)
                student4.add_reward_history_list(reward_info.activities)

            else:
                raise ValueError




class Reward_info(object):
    def __init__(self):
        self.point_reward = 0
        self.activities = ""

    def set_point_reward(self, value):
        self.point_reward = value

    def set_activities(self, activities):
        self.activities = activities

student1 = Student("Justin", "Guo", "00001", 0, [])
student2 = Student("Evan", "Bai","00002", 0, [])
student3 = Student("Jerry", "Cui", "00003", 0, [])
student4 = Student("Waldon", "Zhang", "00004", 0, [])

student_list = Student_list([student1, student2, student3, student4])

reward_info = Reward_info()


