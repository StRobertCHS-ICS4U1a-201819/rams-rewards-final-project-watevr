class Student(object):
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        self.point = 0

    def add_point(self, value):
        self.point += value
        return self.point

class Student_list(object):
    def __init__(self, student_list, point_list):
        self.student_list = student_list
        self.point_list = point_list

    def get_point_value(self, student_name):
        for i in range(len(self.student_list)):
            if student_name == self.student_list[i]:
                return self.point_list[i]

student1 = ("Justin", "Guo", 0)
student2 = ("Evan", "Bai", 0)
student3 = ("Jerry", "Cui", 0)
student4 = ("Waldon", "Zhang", 0)


