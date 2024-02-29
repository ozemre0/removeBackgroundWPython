from rembg import remove
from PIL import Image
# enter your own image with path 
image = Image.open("C:\\Users\\USER\\Desktop\python\\remove_background\\yourimage.jpg")
removed_background = remove(image)
# type how you want your new image to be named
removed_background.save("removedbackgroundimage.png")
