import time
from machine import Pin

# Define the LEDs
ledRED = Pin(4, Pin.OUT)
ledYELLOW = Pin(3, Pin.OUT)
ledGREEN = Pin(5, Pin.OUT)

print("Hello, Pi Pico!")

while True:
    # Red light on
    ledRED.on()
    ledYELLOW.off()
    ledGREEN.off()
    time.sleep(3)

    # Yellow light on
    ledRED.off()
    ledYELLOW.on()
    ledGREEN.off()
    time.sleep(2)

    # Green light on
    ledRED.off()
    ledYELLOW.off()
    ledGREEN.on()
    time.sleep(3)
