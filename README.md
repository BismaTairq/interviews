# 🧪 Real-Time Image Classification Pipeline

A minimal real-time image classification pipeline using **PyTorch**, **OpenCV**, **gRPC**, **Docker**, and **Kafka** (or Redpanda). It simulates live video frame streaming and runs gRPC-based inference using a pretrained ResNet18 model.

---

## Components

- **Inference Service**: A gRPC server using PyTorch's ResNet18 model.
- **Streaming Simulator**: Kafka-based producer (video frame sender) and consumer (calls gRPC).
- **Dockerized Deployment**: Includes multi-stage build and Kafka services via Docker Compose.

---

## Setup Instructions

### Prerequisites

- Python 3.9+
- Docker & Docker Compose installed
- Kafka & Redpanda (via Docker or Docker Compose)
- Webcam or video input source

---

## Getting Started

### Build & Run gRPC Server (Locally)

cd inference_service

# Compile gRPC protobuf definition
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inference.proto

# Start gRPC inference server
python server.py

### Build & Run with Docker

Step 1: Start Kafka + Zookeeper
docker-compose up -d

This will start Kafka and Zookeeper containers in the background. Ensure you have a valid docker-compose.yml file at the root.

Step 2: Build Inference Service Docker Image
docker build -t image-classifier .

Step 3: Run Docker Container
docker run -p 50051:50051 image-classifier

Simulate Video Streaming
Run the following scripts from separate terminals:

Start Kafka Producer
python streaming_simulator/producer.py

Start Kafka Consumer (calls gRPC inference)
python streaming_simulator/consumer.py

Output
- Logs predicted labels for each frame
- Prints latency (inference time per frame)
- Prints average throughput (frames/sec) after 30 seconds

Project Structure
├── inference_service/
│   ├── model.py
│   ├── server.py
│   ├── inference.proto
├── streaming_simulator/
│   ├── producer.py
│   └── consumer.py
│   └── inference_pb2_grpc.py
│   └── inference_pb2.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
