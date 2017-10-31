from digitalio import DigitalInOut, Direction, Pull
import board
import time
import neopixel

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

pixelPin = board.D2
pixelNumber = 8
strip = neopixel.NeoPixel(pixelPin, pixelNumber, brightness=1, auto_write=False)


switch = DigitalInOut(board.D1)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


def wheel(pos):
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)

    if (pos < 85):
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))

def rainbow_cycle(wait):
    for outer in range(255):
        for inner in range(len(strip)):
            index = int((inner * 256 / len(strip)) + outer)
            strip[inner] = wheel(index & 255)
            strip.write()
        time.sleep(wait)


while True:
    if switch.value:
        led.value = False
        strip.fill((0, 0, 0))
        strip.write()
    else:
        led.value = True
        # strip.fill((255, 0, 0))
        rainbow_cycle(0.001)
    # time.sleep(0.01)