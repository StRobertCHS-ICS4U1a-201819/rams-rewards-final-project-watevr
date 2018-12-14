class Student(object):
    def __init__(self, fName, lName, id, point):
        self.fName = fName
        self.lName = lName
        self.id = id
        self.point = point

    def get_fullName(self):
        return self.fName + self.lName

    def add_point(self, value):
        self.point += value
        return self.point

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
                student1.add_point(point_reward.point_reward)

            elif id_value == 2:
                student2.add_point(point_reward.point_reward)


            elif id_value == 3:
                student3.add_point(point_reward.point_reward)


            elif id_value == 4:
                student4.add_point(point_reward.point_reward)

            else:
                raise ValueError




class Point_reward(object):
    def __init__(self):
        self.point_reward = 0

    def set_point_reward(self, value):
        self.point_reward = value

student1 = Student("Justin", "Guo", "00001", 0)
student2 = Student("Evan", "Bai","00002", 0)
student3 = Student("Jerry", "Cui", "00003", 0)
student4 = Student("Waldon", "Zhang", "00004", 0)

student_list = Student_list([student1, student2, student3, student4])

point_reward = Point_reward()


