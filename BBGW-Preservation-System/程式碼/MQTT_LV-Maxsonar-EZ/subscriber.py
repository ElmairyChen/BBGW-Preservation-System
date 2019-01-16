import paho.mqtt.client as mqtt
import Adafruit_BBIO.GPIO as GPIO

pin="P9_14"
GPIO.setup(pin,GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("BBGW")

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    a=float(str(msg.payload))
    if a<400:
       GPIO.output(pin,GPIO.HIGH)
    else:
       GPIO.output(pin,GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.43.253", 1883,10)
client.loop_forever()
