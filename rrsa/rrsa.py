from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Rrsa(BoxLayout):
    student_list = ['Bob Marley', 'Hello']
    full_name_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def view_student_rp(self):
        #view student reward points
        student_name = self.full_name_text_input.text
        password = self.password_text_input.text

        for i in range(len(self.student_list)):
            if self.student_list[i] == student_name:
                print("hello")


    def view_student_info(self):
        pass

    def student_barcode(self):
        pass

    def view_student_history(self):
        pass

class RrsaApp(App):

    def build(self):
        return Rrsa()

rrsaApp = RrsaApp()
rrsaApp.run()