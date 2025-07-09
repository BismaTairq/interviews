from kafka import KafkaConsumer
import base64
import grpc
import inference_pb2_grpc, inference_pb2
import time

consumer = KafkaConsumer('image-stream', bootstrap_servers='localhost:9092')
channel = grpc.insecure_channel('localhost:50051')
stub = inference_pb2_grpc.InferenceServiceStub(channel)

start_time = time.time()
frame_count = 0

for msg in consumer:
    image_bytes = base64.b64decode(msg.value)
    t1 = time.time()
    response = stub.Predict(inference_pb2.ImageRequest(image=image_bytes))
    latency = time.time() - t1
    print(f"Label: {response.label}, Latency: {latency:.3f}s")
    frame_count += 1
    if time.time() - start_time > 30:
        break

print(f"Processed {frame_count} frames in 30s ({frame_count/30:.2f} FPS)")
