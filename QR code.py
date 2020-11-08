import pyqrcode
import png
from pyqrcode import  QRCode

webpage = "https://www.instagram.com/doodle_.rs/"
#Genrating the QR code for the site
url = pyqrcode.create(webpage)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)