# Import QR Code library
import qrcode

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# The data that you want to store
data = "The Data that you need to store in the QR Code"

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# Its always a PNG image

img.save("image.png")


#
import io
imgByteArr = io.BytesIO()
img.save(imgByteArr, format='PNG')
#imgByteArr = imgByteArr.getvalue()