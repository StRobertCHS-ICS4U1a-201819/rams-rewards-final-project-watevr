"""
-------------------------------------------------------------------------------
Name:		Main.py
Purpose:
A mobile app will be used by teacher and administrators to
distribute rewards points to students

Author:		Jerry, Cui & Waldon，Zhang

Created:		2019/01/21
------------------------------------------------------------------------------
"""

import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
import time
import pyzbar.pyzbar as pyzbar
import cv2

import requests
import json
import urllib.request

from kivy.core.text import LabelBase
LabelBase.register(name="fancy", fn_regular="fancy.ttf")
LabelBase.register(name="quick", fn_regular="quick.otf")
LabelBase.register(name="brush", fn_regular="brush.otf")
LabelBase.register(name="letter", fn_regular="grandpaletter.otf")
LabelBase.register(name="violet", fn_regular="violet.otf")
LabelBase.register(name="sig", fn_regular="signature.ttf")
LabelBase.register(name="big", fn_regular="bigbrush.ttf")
LabelBase.register(name="thick", fn_regular="thick.ttf")
LabelBase.register(name="ani", fn_regular="animal.ttf")
LabelBase.register(name="basic", fn_regular="basic.otf")
LabelBase.register(name="hand", fn_regular="hand.ttf")

class RootWidget(TabbedPanel):

    manager = ObjectProperty(None)

    reward_data = ObjectProperty(None)
    reward_activity = ListProperty(None)

    student_data = ObjectProperty(None)
    student_name_list = ListProperty(None)

    activity_selected = ObjectProperty(None)
    activity_order = ObjectProperty(None)
    point = ObjectProperty(None)
    rewardActivity = ObjectProperty(None)

    rewarded_student = ObjectProperty(None)
    student_order = ObjectProperty(None)

    activity_history = ObjectProperty(None)

    date_history = ObjectProperty(None)

    id = ObjectProperty(None)

    def reward(self):
        '''
        A function to use HTTP request all information of reward from Web console and store
        the value of list of activities
        '''

        # request of information of rewards
        req = requests.get('http://10.112.6.115:8000/get_all_reward/')

        print(req.status_code)


        # decode the json file and store the information
        self.reward_data = req.json()

        # extract all activities name into a list
        for reward in self.reward_data['reward_name']:
            self.reward_activity.append(reward)

    def student(self):
        '''
         A function to use HTTP request all information of students from Web console and store
         the value of list of student name
        '''

        # request of information of students
        req = requests.get('http://10.130.182.250:8000/get_all_users/')

        print(req.status_code)

        # decode the json file and store the information
        self.student_data = req.json()

        # extract all students' name into a list
        for student in self.student_data['user_name']:
            self.student_name_list.append(student)



    def switch_to(self, header):
        '''
         A function to control the screen
        '''

        # set the Screen manager to load  the appropriate screen
        # linked to the tab head instead of loading content
        self.manager.current = header.screen
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header

    def spinner_clicked(self, activities_name):
        '''Set the related point and name of activity, while depending on the activity that teacher chose

         :param: the name of activities that administrator selected
         '''

        # use for loop and if statement to find the order of the activity in the reward data and
        # store the information of particular activity and order
        for i in len(self.reward_data['reward_name']):
            if self.reward_data[i]['reward_name'] == activities_name:
                self.activity_selected = self.reward_data[i]
                self.activity_order = i
                break

        # store the point and name of activity
        self.point = self.activity_selected['points']
        self.rewardActivity = activities_name

    def id_inputted(self):
        '''Set the related point and name of activity, while depending on the activity that teacher chose

        :param: the name of activities that administrator selected
        '''

        # use  for loop and if statement to find the order of the student id in the student data and
        # store the information of particular student and order
        for i in len(self.student_data['id']):
            if self.student_data[i]['id'] == self.id:
                self.rewarded_student = self.student_data[i]
                self.student_order = i
                break

        # add related point and record activity to student file
        self.rewarded_student['points'] += self.point
        self.rewarded_student['rewarded_history'].append(self.rewardActivity)

        # add student id to activity information
        self.activity_selected['student'].append(self.id)

        # refresh the student data with the new one and dump back to json file
        self.student_data[self.student_order] = self.rewarded_student
        with open('new_student_data.json', 'w') as f:
            json.dump(self.student_data, f)


    def add_date(self, date):
        '''Set the date of activity occur

        :param: the name of activities that administrator selected
        '''

        # record date to activity information
        self.activity_selected[date].append(date)

        # refresh the student data with the new one and dump back to json file
        self.reward_data[self.activity_order] = self.activity_selected
        with open('new_reward_data.json', 'w') as f:
            json.dump(self.reward_data, f)


    def spinner_clicked2(self, student_name):
        ''' set activity of student that the administrator want to check

        :param: the name of student
        '''

        # use for loop and if statement to get name of activity that student attended and
        # store the value
        for i in len(self.student_data['user_name']):
            if self.student_data[i]['reward_name'] == student_name:
                self.activity_history = self.reward_data[i]['activity']
                break

    def spinner_clicked3(self, activity_name):
        ''' set date of activity that the administrator want to check

        :param: the name of activity
        '''

        # use for loop and if statement to get date of activity that activity occur and
        # store the value
        for i in len(self.reward_data['date']):
            if self.reward_data[i]['date'] == activity_name:
                self.date_history = self.reward_data[i]['date']
                break

    def dostart(self, *largs):
        ''' start the camera

        '''
        global capture
        capture = cv2.VideoCapture(0)
        self.ids.qrcam.start(capture)

    def capture(self):
        '''
        Function to capture the images and read the information

        '''

        ret, frame = capture.read()
        # change color to grey
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # decode the barcode
        barcodes = pyzbar.decode(gray)

        for barcode in barcodes:
            # extract the position of QR code and draw its frame
            (x, y, w, h) = barcode.rect
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)


            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type


            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(gray, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        .5, (0, 0, 125), 2)

            # set student id that gain from scanning process
            self.id = barcodeData


class KivyCamera(Image):

    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = None

    def start(self, capture, fps=30):
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def stop(self):
        Clock.unschedule_interval(self.update)
        self.capture = None

    def update(self, dt):
        return_value, frame = self.capture.read()
        if return_value:
            texture = self.texture
            w, h = frame.shape[1], frame.shape[0]
            if not texture or texture.width != w or texture.height != h:
                self.texture = texture = Texture.create(size=(w, h))
                texture.flip_vertical()
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.canvas.ask_update()


class QrtestHome(BoxLayout):
    def init_qrtest(self):
        pass

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)

class CombineApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    CombineApp().run()