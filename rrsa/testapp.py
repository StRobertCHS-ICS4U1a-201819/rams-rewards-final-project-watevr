from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from qrcodewidget import QRCodeWidget


class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):

    student_list = ["t", "helloworld", "bobby5000", "coolkid24"]
    student_password_list = ["t", "helloworld123", "password123", "password24"]
    student_reward_points = [0, 0, 0]
    student_homeroom = [None, None, None]
    student_id = [123, 321, 213]
    uname = ObjectProperty()
    pword = ObjectProperty()

    def login(self):
        uname = self.uname.text
        pword = self.pword.text
        for i in range(len(self.student_list)):
            if self.student_list[i] == uname and self.student_password_list[i] == pword:
                self.parent.current = 'homepage'
                self.uname.text = ''
                self.pword.text = ''
                break
        else:
            self.login_fail()



    def login_fail(self):
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(text="Incorrect Username or Password. \n                   Try Again."))
        popup = Popup(title='Error', title_size=(30),
                      title_align='center', content=box,
                      size_hint=(None, None), size=(400, 300),
                      auto_dismiss=False)
        box.add_widget(Button(text="Press to close", on_press=popup.dismiss))
        popup.open()



class HomePage(Screen):

    def logout(self):
        self.parent.current = 'main_screen'

    def to_rewards(self):
        self.parent.current = 'rewards_history'

    def to_info(self):
        self.parent.current = 'student_info'

    def qr_code(self):
        self.parent.current = 'qr_code'

class RewardsHistory(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RewardsHistory, self).__init__(**kwargs)
        Clock.schedule_once(self.setup_scrollview, 1)

    def setup_scrollview(self, dt):
        self.container.bind(minimum_height=self.container.setter('height'))
        self.add_text_inputs()

    def add_text_inputs(self):
        for x in range(20):
            self.container.add_widget(Label(text="Reward Activity {}     Points Earned: ".format(x), size_hint_y=None, height=60))

    def to_homepage(self):
        self.parent.current = 'homepage'

class StudentInfo(Screen):

    def to_homepage(self):
        self.parent.current = 'homepage'

class StudentQRCode(Screen):

    def qr_code(self):
        box = BoxLayout(orientation='vertical', padding=(10))
        popup = Popup(title="QRCode", content=box, size_hint=(None, None),
                      size=(500, 500), auto_dismiss=True)
        box.add_widget(QRCodeWidget(data="Student qrcode"))
        popup.open()

    def to_homepage(self):
        self.parent.current = 'homepage'

class TestApp(App):
    title = "RRSA"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    TestApp().run()