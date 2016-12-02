import time
import paho.mqtt.client as mqtt
import random

mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

#read temperature
def read_pollutants():
    return random.randint(0, 100)

#publish temperature
while 1:
    t=read_pollutants()
    (result,mid)=mqttc.publish("topic/GeneralizedIoT/pollutants",t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()