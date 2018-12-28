import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):



    def spinner_clicked(self, value):
        print("Spinner Value " + value)


class Screen1App(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return SampBoxLayout()

Screen1_app = Screen1App()
Screen1_app.run()