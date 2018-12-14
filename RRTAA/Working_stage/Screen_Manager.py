import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


from RRTAA.package import RewardActivities

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def spinner_clicked(self, value):

        print(RewardActivities.reward.get_point_value(value))
        print("Spinner Value " + value)

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

class AnswerInput(BoxLayout):
    textinput = TextInput(text='Hello world')

    def on_enter(instance, value):
        print('User pressed enter in', instance)

    textinput = TextInput(text='Hello world', multiline=False)
    textinput.bind(on_text_validate=on_enter)




ScreensApp().run()