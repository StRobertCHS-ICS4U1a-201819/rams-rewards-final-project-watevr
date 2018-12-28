import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.lang import Builder



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

class Combine0App(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    Combine0App().run()