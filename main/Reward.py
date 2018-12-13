import Classroom
import Student

activity = open("RewardActivity.txt", "r+")
activities = activity.readlines()
activity_list = []
log_in = False                                      #the state of login
													#add acitvities to list from the txt file
for lst in activity:							
	activity_list.append(lst.spilt(","))


def reward(student_id, acitvitiyNumber):
	teacher_id = input("Please input your ID: ")
	password = input("Please input your password: ")
	if teacher_id == Teacher.teacher_id and password == Teacher.teacher_password:
		log_in = true

	while log_in == true:
		student_ID = student_id
		actnum = acitvitiyNumber
		for act in activity_list:
			if actnum == act[0]:
				student_points += int(act[2])

