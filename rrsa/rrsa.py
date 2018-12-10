from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class Rrsa(BoxLayout):
    student_list = ["Bob Marley", "Bob Bob", "Bobby Bob"]
    student_password_list = ["Bob123", "Bob321", "Bob231"]
    student_reward_points = [0, 0, 0]
    full_name_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def login_success(self):
        student_name = self.full_name_text_input.text
        student_password = self.password_text_input.text
        content = Button(text='Click here to escape')
        popup = Popup(title='Login Successful to ' + student_name, title_size=30,
                      content=content,
                      size_hint=(.3, .3), size=(400, 400))
        content.bind(on_press=popup.dismiss)
        for i in range(len(self.student_list)):
            if self.student_list[i] == student_name and self.student_password_list[i] == student_password:
                popup.open()


    def view_student_info(self):
        pass

    def student_barcode(self):
        pass

    def view_student_history(self):
        pass


class Popup(Popup):
    pass

class RrsaApp(App):

    def build(self):
        return Rrsa()

rrsaApp = RrsaApp()
rrsaApp.run()