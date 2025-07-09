import cv2
from kafka import KafkaProducer
import base64

producer = KafkaProducer(bootstrap_servers='localhost:9092')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    encoded = base64.b64encode(buffer).decode('utf-8')
    producer.send('image-stream', value=encoded.encode('utf-8'))
