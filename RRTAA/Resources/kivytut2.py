import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




Builder.load_string('''
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to Screen 2"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"
    
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: "Reward Activities"
    Button:
        text: "Highest Mark"
        on_press: root.dismiss()
    Button:
        text: "Average over 85"
        on_press: root.dismiss()
    Button:
        text: "Club Meeting"
        on_press: root.dismiss()
    Button:
        text: "Sport Team"
        on_press: root.dismiss()
    Button:
        text: "Activities Leader"
        on_press: root.dismiss()
    
    BoxLayout:
        orientation: "horizontal"
        height: 30
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            Spinner:
                text: "Reward Activities"
                values: ["Highest Mark", "Average over 85", "Club Meeting", "Sport Team", "Activities Leader"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)

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

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class KivyTut2App(App):

    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()