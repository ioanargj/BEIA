import paho.mqtt.client as mqtt
import psutil
import json
import time

MQTT_server="mqtt.beia-telemetrie.ro"
MQTT_port=1883

def main():
    client=mqtt.Client()
    client.connect(MQTT_server, MQTT_port, 60)
    
    while True:
        topic = 'citisim/raspberry/IoanaPiZero'
        mem = psutil.virtual_memory()
        data = {'availableMemory':mem.available,
                'freeMemory':mem.free,
                'usedMemory':mem.used,
                }
        
        payload = json.dumps(data)
        print("Topic: {0}".format(topic))
        print("Payload: {0}".format(payload))
        client.publish(topic, payload=payload,qos=1)
        
        time.sleep(10)

if __name__ == '__main__':
    main()
    

