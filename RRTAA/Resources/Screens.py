import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

from RRTAA.package import RewardActivities
from RRTAA.package import Student


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def spinner_clicked(self, acitivies_name):
        value = RewardActivities.reward.get_point_value(acitivies_name)
        Student.point_reward.set_point_reward(value)
        print(value, Student.point_reward.point_reward)

        print("Spinner Value " + acitivies_name)

    def id_inputted(self, id):
        Student.student_list.get_student_object(id)
        print(Student.student1.point)
        print(Student.student2.point)


class ScreenThree(Screen):

    def student_scanner(self):
        value = "Jerry Cui"

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(App):
    def build(self):
        return Manager()



ScreensApp().run()