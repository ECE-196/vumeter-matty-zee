#EXTRA CREDIT SOLUTION
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)
status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]
for led in leds:
    led.direction = Direction.OUTPUT

decay_rate = 0.1  

while True:
    volume = microphone.value
    volume_percent = int((volume - 25000) / 25000 * 100)
    if volume_percent < 0:
        volume_percent = volume_percent * -1

    # print(volume_percent)

    target_num_leds_on = volume_percent // 11

    for i in range(len(leds)):
        if i < target_num_leds_on:
            leds[i].value = True
        else:
            for j in range(len(leds)-1, 0, -1):
                if leds[j].value:
                    leds[j].value = False
                    sleep(decay_rate)  