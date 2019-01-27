
import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
import time
import pyzbar.pyzbar as pyzbar
import cv2
from kivy.base import EventLoop
from RRTAA.package import RewardActivities
from RRTAA.package import Student
from kivy.core.text import LabelBase
LabelBase.register(name="fancy", fn_regular="fancy.ttf")
LabelBase.register(name="quick", fn_regular="quick.otf")
LabelBase.register(name="brush", fn_regular="brush.otf")
LabelBase.register(name="letter", fn_regular="grandpaletter.otf")
LabelBase.register(name="violet", fn_regular="violet.otf")
LabelBase.register(name="sig", fn_regular="signature.ttf")
LabelBase.register(name="big", fn_regular="bigbrush.ttf")
LabelBase.register(name="thick", fn_regular="thick.ttf")
LabelBase.register(name="ani", fn_regular="animal.ttf")
LabelBase.register(name="basic", fn_regular="basic.otf")
LabelBase.register(name="hand", fn_regular="hand.ttf")


class RootWidget(TabbedPanel):

   manager = ObjectProperty(None)

   reward_history1 = ObjectProperty(None)
   reward_history2 = ObjectProperty(None)
   reward_history3 = ObjectProperty(None)
   reward_history4 = ObjectProperty(None)

   date_history1 = ObjectProperty(None)
   date_history2 = ObjectProperty(None)
   date_history3 = ObjectProperty(None)
   date_history4 = ObjectProperty(None)
   date_history5 = ObjectProperty(None)

   reward_history = ObjectProperty(None)
   date_history = ObjectProperty(None)


   def switch_to(self, header):
       # set the Screen manager to load  the appropriate screen
       # linked to the tab head instead of loading content
       self.manager.current = header.screen
       # we have to replace the functionality of the original switch_to
       self.current_tab.state = "normal"
       header.state = 'down'
       self._current_tab = header

   def spinner_clicked1(self, acitivies_name):
       value = RewardActivities.reward.get_point_value(acitivies_name)

       print(value)

       Student.reward_info.set_point_reward(value)
       Student.reward_info.set_activities(acitivies_name)

   def spinner_clicked2(self, acitivies_name):
       self.reward_history = "Highest Mark"

   def spinner_clicked3(self, acitivies_name):
       self.date_history = "Oct 13"



   def id_inputted(self, id):
       print(id)
       Student.student_list.get_student_object(id)

       print(Student.student1.point)
       print(Student.student2.point)
       print(Student.student3.point)
       print(Student.student4.point)

   def set_student_history(self):
       self.reward_history1 = Student.student1.reward_history_list
       self.reward_history2 = Student.student2.reward_history_list
       self.reward_history3 = Student.student3.reward_history_list
       self.reward_history4 = Student.student4.reward_history_list

       print(self.reward_history1)
       print(self.reward_history2)
       print(self.reward_history3)
       print(self.reward_history4)

   def add_date(self, val_date):
       Student.reward_info.set_date_list(val_date)

   def set_date_history(self):
       self.date_history1 = Student.activities1.date_list
       self.date_history2 = Student.activities2.date_list
       self.date_history3 = Student.activities3.date_list
       self.date_history4 = Student.activities4.date_list
       self.date_history5 = Student.activities5.date_list

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
   def dostart(self, *largs):
       global capture
       capture = cv2.VideoCapture(0)
       self.ids.qrcam.start(capture)


   def doexit(self):
       global capture
       if capture != None:
           capture.release()
           capture = None
       EventLoop.close()

   def capture(self):
       '''
       Function to capture the images and give them the names
       according to their captured time and date.
       '''
       camera = self.ids['qrcam']
       timestr = time.strftime("%Y%m%d_%H%M%S")
       ret, frame = capture.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       barcodes = pyzbar.decode(gray)
       for barcode in barcodes:
           (x, y, w, h) = barcode.rect
           cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)


           barcodeData = barcode.data.decode("utf-8")
           barcodeType = barcode.type


           text = "{} ({})".format(barcodeData, barcodeType)
           cv2.putText(gray, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                       .5, (0, 0, 125), 2)


           print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
           print(text)


class KivyCamera(Image):

   def __init__(self, **kwargs):
       super(KivyCamera, self).__init__(**kwargs)
       self.capture = None

   def start(self, capture, fps=30):
       self.capture = capture
       Clock.schedule_interval(self.update, 1.0 / fps)

   def stop(self):
       Clock.unschedule_interval(self.update)
       self.capture = None

   def update(self, dt):
       return_value, frame = self.capture.read()
       if return_value:
           texture = self.texture
           w, h = frame.shape[1], frame.shape[0]
           if not texture or texture.width != w or texture.height != h:
               self.texture = texture = Texture.create(size=(w, h))
               texture.flip_vertical()
           texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
           self.canvas.ask_update()




class QrtestHome(BoxLayout):
   def init_qrtest(self):
       pass






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
