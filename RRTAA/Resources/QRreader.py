from qrtools.qrtools import QR

my_QR = QR(filename = "home/user/Desktop/QR.jpg")

my_QR.decode()

print(my_QR.data)