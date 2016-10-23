from kafka import KafkaConsumer
import base64


consumer = KafkaConsumer('hello_world')

for msg in consumer:
 print (msg.value)
 img=base64.b64decode(msg.value)
 print(img)