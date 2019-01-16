import paho.mqtt.client as mqtt
import Adafruit_BBIO.ADC as ADC
import time

_g_cst_ToMQTTTopicServerIP = "192.168.43.253"
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName = "BBGW" #TOPIC name

ADC.setup()

while True:

    a=ADC.read_raw("P9_39")
    mqttc = mqtt.Client("python_pub")
    mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
    mqttc.publish(_g_cst_MQTTTopicName, str(a))
    time.sleep(1)
