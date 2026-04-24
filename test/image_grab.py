import window
from PIL import ImageGrab

window.activate_window("동방")

coordinate = [0, 0, 100, 200]

img = ImageGrab.grab(bbox=(coordinate))
img.show()