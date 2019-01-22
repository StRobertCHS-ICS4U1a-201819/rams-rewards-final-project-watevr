from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):

    uname = ObjectProperty()
    pword = ObjectProperty()

    def login(self):
        uname = self.uname.text
        pword = self.pword.text
        if uname == "test" and pword == "test":
            self.parent.current = 'homepage'
            self.uname.text = ''
            self.pword.text = ''
        else:
            self.login_fail()

    def login_fail(self):
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(text="Incorrect Username or Password. \n Try Again."))
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
            self.container.add_widget(Label(text="Reward Activity {}".format(x), size_hint_y=None, height=60))

    def to_homepage(self):
        self.parent.current = 'homepage'

class TestApp(App):
    title = "RRSA"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    TestApp().run()