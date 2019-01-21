import qrtools.qrtools
qr = qrtools.QR()
qr.decode("QR.jpg")
print(qr.data)