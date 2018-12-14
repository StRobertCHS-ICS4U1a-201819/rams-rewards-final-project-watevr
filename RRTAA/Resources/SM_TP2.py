import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from RRTAA.package import RewardActivities
from RRTAA.package import Student

class RootWidget(TabbedPanel):

    manager = ObjectProperty(None)

    def switch_to(self, header):
        # set the Screen manager to load  the appropriate screen
        # linked to the tab head instead of loading content
        self.manager.current = header.screen
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header
    def spinner_clicked(self, acitivies_name):
        value = RewardActivities.reward.get_point_value(acitivies_name)
        Student.point_reward.set_point_reward(value)
        print(value, Student.point_reward.point_reward)

        print("Spinner Value " + acitivies_name)

    def id_inputted(self, id):
        Student.student_list.get_student_object(id)
        print(Student.student1.point)

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
    screen_three = ObjectProperty(None)

class Combine1App(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    Combine1App().run()