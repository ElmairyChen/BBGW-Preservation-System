from __future__ import print_function
#!/usr/bin/env python

import time
import mraa
import Adafruit_BBIO.GPIO as GPIO
from __future__ import print_function
import paho.mqtt.publish as publish


channelID = "648766"
apiKey = "Q6BYTE7UI3NH902K"
useUnsecuredTCP = False
useUnsecuredWebsockets = False
useSSLWebsockets = True
mqttHost = "mqtt.thingspeak.com"
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443
        
# Create the topic string
topic = "channels/" + channelID + "/publish/" + apiKey
# build the payload string
tPayload = "field1=" + str(1)

Buzzer = 68            # GPIO P9_22
PIR = 67               # GPIO P9_21

pir = mraa.Gpio(PIR)
buzzer = mraa.Gpio(Buzzer)

pir.dir(mraa.DIR_IN)
buzzer.dir(mraa.DIR_OUT)
GPIO.setup("P9_22", GPIO.OUT)
motion=0

while True:
	try:
		# Sense motion, usually human, within the target range
		motion=pir.read()
		if motion==0 or motion==1:	# check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
			if motion==1:
				print ('Attention there is intruder.')
				publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
				GPIO.output("P9_22", GPIO.HIGH)
				time.sleep(2)
			else:
				print ('-')

			# if your hold time is less than this, you might not see as many detections
		time.sleep(.2)


	except KeyboardInterrupt:

            GPIO.output("P9_22", GPIO.LOW)

            print 'Program stop'

            break

	except IOError:
		print ("Error")