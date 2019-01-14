import win32com.client  #https://sourceforge.net/projects/pywin32/
import pythoncom
import time

class EvHandler:
    def OnBarcodeIn(self, _1):
        print(_1);

scanner = win32com.client.DispatchWithEvents("BarcodeScanner.Reader", EvHandler)
scanner.Visible = True

while 1:
    pythoncom.PumpWaitingMessages()
    time.sleep(0.8) # Don't use up all our CPU checking constantly