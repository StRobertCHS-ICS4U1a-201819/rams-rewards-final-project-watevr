from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.garden.qrcode import QRCodeWidget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Rrsa(BoxLayout):
    #testing lists by putting in placeholders
    student_list = ["Bob Marley", "Bob Bob", "Bobby Bob"]
    student_password_list = ["Bob123", "Bob321", "Bob231"]
    student_reward_points = [0, 0, 0]
    student_homeroom = [None, None, None]
    student_id = [123, 321, 213]
    full_name_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def login_success(self):
        student_name = self.full_name_text_input.text
        student_password = self.password_text_input.text
        content = Button(text='Click here to escape')
        popup = Popup(title='Login Successful to ' + student_name, title_size=30,
                      content=content, size_hint=(.3, .3), size=(400, 400))
        content.bind(on_press=popup.dismiss)
        for i in range(len(self.student_list)):
            if self.student_list[i] == student_name and self.student_password_list[i] == student_password:
                popup.open()

    def view_student_rp(self):
        student_name = self.full_name_text_input.text
        student_password = self.password_text_input.text
        for i in range(len(self.student_list)):
            if self.student_list[i] == student_name and self.student_password_list[i] == student_password:
                reward_points = self.student_reward_points[i]
                popup = Popup(title='Student Reward Points',
                              title_size=16, content=Label(text=student_name + "'s Reward Points: " +
                              str(reward_points)), size_hint=(.5, .3), size=(400, 400))
                popup.open()

    def view_student_info(self):
        student_name = self.full_name_text_input.text
        student_password = self.password_text_input.text

        for i in range(len(self.student_list)):
            if self.student_list[i] == student_name and self.student_password_list[i] == student_password:
                homeroom = self.student_homeroom[i]
                id = self.student_id[i]

                popup = Popup(title='Student Info', title_size=32,
                              content=Label(text='Full Name: ' + student_name + '\n\n Homeroom: ' +
                              str(homeroom) + '\n\n id: ' + str(id), size_hint_y=.9),
                              size_hint=(.4, .4), size=(400, 400))
                popup.open()

    def student_barcode(self):
        pass

    def view_student_history(self):
        pass

class RrsaApp(App):

    def build(self):
        return Rrsa()

rrsaApp = RrsaApp()
rrsaApp.run()