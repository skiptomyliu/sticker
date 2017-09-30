import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


WHITE_LINE = 17
GREEN_LINE = 22
BLUE_LINE = 18
RED_LINE = 23

GPIO.setup(WHITE_LINE, GPIO.OUT)
GPIO.setup(GREEN_LINE, GPIO.OUT)
GPIO.setup(BLUE_LINE, GPIO.OUT)
GPIO.setup(RED_LINE, GPIO.OUT)

is_on = False


def set_step(wht, grn, red, blu):
    GPIO.output(WHITE_LINE, wht)
    GPIO.output(GREEN_LINE, grn)
    GPIO.output(RED_LINE, red)
    GPIO.output(BLUE_LINE, blu)


def backward(delay, steps):
    for i in range(0, steps):
        set_step(1, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(1, 0, 1, 0)
        time.sleep(delay)

def forward(delay, steps):
    for i in range(0, steps):
        set_step(1, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(1, 0, 0, 1)
        time.sleep(delay)

forward(2/1000.0, 500)
