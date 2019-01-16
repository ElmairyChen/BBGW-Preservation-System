import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

ADC.setup()
pin="P9_14"
GPIO.setup(pin,GPIO.OUT)

while True:
    a=ADC.read_raw("P9_39")
    #print(a)
    if(a<1000):
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)
