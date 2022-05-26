import qrcode
import cv2

# generating qrcode of google.com
img = qrcode.make("https://www.google.com/")#make() retruns qr image
img.save("google.jpg")

#decoding the qr code
detector = cv2.QRCodeDetector()
val, points, straight_qrcode = detector.detectAndDecode(cv2.imread("google.jpg"))
print(val) #returns the decoded value of code

