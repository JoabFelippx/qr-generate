import qrcode
from PIL import Image


# https://twitter.com/home


# gerar qrcode
qr = qrcode.QRCode()
qr.add_data("https://twitter.com/home")
qr.make(fit=True)


# gerar image com qrcode
img = qr.make_image(fill_color='black', back_color='white')

img.show()