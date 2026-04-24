
from PIL import ImageGrab

coordinate = [0, 0, 100, 200]

img = ImageGrab.grab(bbox=(coordinate))
img.show()