from PIL import ImageGrab
from PIL import ImageColor
from PIL import Image
import keyboard

def catchScreen(posW,posN,posE,posS):
    im = ImageGrab.grab((posW,posN,posE,posS))
    px=im.load()
    if px[110,50]==ImageColor.getrgb("#535353") or px[110,50]==ImageColor.getrgb("#FFF7F7"):
        keyboard.press_and_release('space')

# catchScreen(400,180,700,330)
while True:
    catchScreen(400,180,700,330)
    if keyboard.is_pressed('esc'):
        break
