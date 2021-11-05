import qrcode
img = qrcode.make("India is a country with many religions. I love India.")
img.save("QR_image.jpg")

import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("QR_image.jpg"))
print("Decoded text is: ", val)