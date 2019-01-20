from qrtools import QR

my_QR = QR(filename = "home/user/Desktop/qr.png")

my_QR.decode()

print(my_QR.data)