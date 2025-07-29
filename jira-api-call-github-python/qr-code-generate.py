import qrcode

data = input("Enter the data to encode in QR code: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
print("QR code generated and saved as 'qrcode.png'.")