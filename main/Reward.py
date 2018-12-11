import Classroom
import Students
import Teachers

activity = open("RewardActivity.txt", "r+")
activities = activity.readlines()
activity_list = []
													#add acitvities to list from the txt file
for lst in activity:							
	activity_list.append(lst.spilt(","))


def reward(student, points):
	teacher_id = input("Please input your ID: ")
	password = input("Please input your password: ")
	if teacher_id == Teacher.teacher_id and password == Teacher.teacher_password
