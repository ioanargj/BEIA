import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time

MQTT_server="mqtt.beia-telemetrie.ro"
MQTT_port="1883"

client=mqtt.Client()
client.connect(MQTT_server, MQTT_port, 60)

while True:
    data="Hello from Raspberry Pi!"
    print(data)

    try:
        client.publish("pi",data)#pi is topic
        time.sleep(10)
    except KeyboardInterrupt:
        print("end")  
client.disconnect()
