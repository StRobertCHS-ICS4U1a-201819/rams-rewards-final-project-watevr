'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time

import pyzbar.pyzbar as pyzbar



class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        barcodes = pyzbar.decode(camera)

        barcodeData = barcodes.data.decode("utf-8")
        barcodeType = barcodes.type

        text = "{} ({})".format(barcodeData, barcodeType)

        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        print(text)
        print("Captured")


class TestCamera2App(App):

    def build(self):
        return CameraClick()


TestCamera2App().run()