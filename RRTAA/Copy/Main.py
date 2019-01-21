import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.image import Image

import requests
import json



from RRTAA.package import RewardActivities
from RRTAA.package import Student

class RootWidget(TabbedPanel):

    manager = ObjectProperty(None)

    reward_data = ObjectProperty(None)
    reward_activity = ObjectProperty(None)

    student_data = ObjectProperty(None)
    student_name_list = ObjectProperty(None)

    activity_selected = ObjectProperty(None)
    activity_order = ObjectProperty(None)
    point = ObjectProperty(None)

    rewarded_student = ObjectProperty(None)
    student_order = ObjectProperty(None)

    activity_history = ObjectProperty(None)

    date_history = ObjectProperty(None)



    def reward(self):

        # we define a request object that is equal to requests.get('API')
        req = requests.get('http://localhost:8000/get_single_reward/1/')
        # we then print out the http status_code that was returned on making this request
        # you should see a successful '200' code being returned.
        print(req.status_code)

        self.reward_data = json.loads(req)

        for reward in self.reward_data['reward']:
            self.reward_activity.append(reward)




    def student(self):

        # we define a request object that is equal to requests.get('API')
        req = requests.get('http://localhost:8000/get_single_reward/1/')
        # we then print out the http status_code that was returned on making this request
        # you should see a successful '200' code being returned.
        print(req.status_code)

        self.student_data = json.loads(req)

        for student in self.student_data['user_name']:
            self.student_name_list.append(student)


    def switch_to(self, header):
        # set the Screen manager to load  the appropriate screen
        # linked to the tab head instead of loading content
        self.manager.current = header.screen
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header

    def spinner_clicked(self, activities_name):

        for i in len(self.reward_data['reward_name']):
            if self.reward_data[i]['reward_name'] == activities_name:
                self.activity_selected = self.reward_data[i]
                self.activity_order = i

        self.point = self.activity_selected['points']

        self.rewardActivity = activities_name

    def id_inputted(self, id):

        for i in len(self.student_data['id']):
            if self.student_data[i]['id'] == id:
                self.rewarded_student = self.student_data[i]
                self.student_order = i
                break

        self.rewarded_student['points'] += 1
        self.activity_selected['student'].append(id)


        self.student_data[self.student_order] = self.rewarded_student

        with open('new_student_data.json', 'w') as f:
            json.dump(self.student_data, f)


    def add_date(self, date):
        self.activity_selected[date].append(date)

        self.reward_data[self.activity_order] = self.activity_selected
        with open('new_reward_data.json', 'w') as f:
            json.dump(self.reward_data, f)


    def spinner_clicked2(self, student_name):
        for i in len(self.student_data['user_name']):
            if self.student_data[i]['reward_name'] == student_name:
                self.activity_history = self.reward_data[i]['activity']
                break

    def spinner_clicked2(self, activity_name):
        for i in len(self.reward_data['date']):
            if self.reward_data[i]['date'] == activity_name:
                self.date_history = self.reward_data[i]['date']
                break




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