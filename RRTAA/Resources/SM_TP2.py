import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder

from RRTAA.package import RewardActivities
from RRTAA.package import Student

class RootWidget(TabbedPanel):

    manager = ObjectProperty(None)
    reward_history1 = ObjectProperty(None)
    reward_history2 = ObjectProperty(None)
    reward_history3 = ObjectProperty(None)
    reward_history4 = ObjectProperty(None)

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

        Student.reward_info.set_point_reward(value)
        Student.reward_info.set_activities(acitivies_name)

        print(value, Student.reward_info.point_reward)

        print("Spinner Value " + acitivies_name)

    def id_inputted(self, id):
        Student.student_list.get_student_object(id)



    def set_student_history(self):
        self.reward_history1 = Student.student1.reward_history_list
        self.reward_history2 = Student.student2.reward_history_list
        self.reward_history3 = Student.student3.reward_history_list
        self.reward_history4 = Student.student4.reward_history_list

    def bubbprint(self, message):
        message = repr(message)
        if not self.info_bubble:
            self.info_bubble = Factory.InfoBubble()
        self.info_bubble.message = message

        # Check if bubble is not already on screen
        if not self.info_bubble.parent:
            Window.add_widget(self.info_bubble)

        # Remove bubble after 2 secs
        Clock.schedule_once(lambda dt:
                            Window.remove_widget(self.info_bubble), 2)

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

class Combine1App(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    Combine1App().run()