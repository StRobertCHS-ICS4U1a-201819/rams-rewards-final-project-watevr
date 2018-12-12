import kivy
kivy.require("1.10.1")

from main import RewardsActivities

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def spinner_clicked(self, value):
        point = value.get_point_value
        print("Spinner Value " + point)

class ScreenThree(Screen):
    pass

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(App):
    def build(self):
        return Manager()

class Reward(object):
    def __int__(self, activities, fullName):
        self.act = activities
        self.fullName = fullName


ScreensApp().run()