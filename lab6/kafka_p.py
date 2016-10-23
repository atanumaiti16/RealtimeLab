
from kafka import KafkaProducer

import base64


with open("/home/atanu/PycharmProjects/lab6/siftframes/sift_keypoints0.jpg", "rb") as image_file:
     encoded_string = base64.b64encode(image_file.read())

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send("hello_world",encoded_string)
