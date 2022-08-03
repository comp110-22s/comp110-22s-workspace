"""Dope program for making qr codes! Didn't exactly figure it out."""

import pyqrcode
# from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/watch?v=-84xlJJv_Bs&t=41s&ab_channel=UNCDarkside"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
# url.svg("myyoutube.svg", scale=8) 

# QRCode
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))