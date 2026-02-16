import qrcode
from qrcode.constants import ERROR_CORRECT_L

""" # Variable qui va conntenir l'image du QR code
img = qrcode.make('Boubacar')
img.save('qrcode.png')
 """

qr = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    
)