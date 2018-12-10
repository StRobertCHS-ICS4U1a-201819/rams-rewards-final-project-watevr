import kivy
kivy.require("1.10.1")

import Classroom

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def spinner_clicked(self, value):
        print("Spinner Value " + value)

class ScreenThree(Screen):
    pass

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(App):
    def build(self):
        return Manager()


ScreensApp().run()