import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup




Builder.load_string('''
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to Screen 2"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_three"
    
<ScreenThree>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    BoxLayout:
        orientation: "horizontal"

        BoxLayout:
            orientation: "horizontal"
            size_hint: .25, .15
        
            Spinner:
                text: "Reward Activities"
                values: ["Highest Mark", "Average over 85", "Club Meeting", "Sport Team", "Activities Leader"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)
            
            Button:
                text: "Go to Scanner Section"
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.transition.duration = 1
                    root.manager.current = "screen_two"

<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to Screen 1"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_one"
''')

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class CustomPopup(Popup):
    pass

    class SampBoxLayout(BoxLayout):

        def spinner_clicked(self, value):
            print("Spinner Value " + value)



screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))


class KivyTut2App(App):

    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()



