from gpiozero import LED
from time import sleep

led=LED(17)

led.on()

sleep(4)

led.off()
