import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

from RRTAA.package import RewardActivities

class Test(TabbedPanel):
    def spinner_clicked(self, value):

        print(RewardActivities.reward.get_point_value(value))
        print("Spinner Value " + value)

    def id_inputted(self, value):
        print("student id" + value)

class TextInputApp(App):
    def build(self):
        return Test()



if __name__ == '__main__':
    TextInputApp().run()