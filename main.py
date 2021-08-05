import qrcode
from PIL import Image


# https://twitter.com/home


# gerar qrcode
qr = qrcode.QRCode()
qr.add_data("https://twitter.com/home")
qr.make(fit=True)

# gerar image com qrcode
img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
img.save('./qr-code/qr-code.png')

# colocar logo no meio do qr
logo = Image.open('./logo/twitter-logo.png')
logo.thumbnail((60, 60))

logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
print(logo_pos)

img.paste(logo, logo_pos)
img.save('./qr-code/qr-code_with_logo.png')
img.show()
