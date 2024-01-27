import qrcode
from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #grabs current date and time
str_current_datetime = str(current_datetime) # convert datetime obj to string

webSite = input("Please type in your URL: ") #asks user to type in the URL they want to generate code from

img = qrcode.make(webSite) #generates the qr image
type(img)  # qrcode.image.pil.PilImage
img.save("url_" + str_current_datetime + ".png") #saves the image to the local director
print("Created QR Code!") #printout message in terminal to confirm program ran all the way through
