import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=2)
qr.add_data('https://codeanddebug.in')
qr.make(fit=True)
img = qr.make_image(image_factory= StyledPilImage, module_drawer=RoundedModuleDrawer())
img.save("myQRcode3.png")