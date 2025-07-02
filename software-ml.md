# Kookree ML Systems Engineer – Technical Assignment

Welcome! This short technical assignment is designed to evaluate your skills in model deployment, containerization, streaming, and system optimization—core to what we do at Kookree.

You are expected to build a minimal real-time image classification pipeline using PyTorch, OpenCV, Docker, and gRPC, with simulated streaming input via Kafka or Redpanda.

---

## 🧪 Assignment Overview

### Task Summary

- Serve a PyTorch image classification model over a **gRPC** API.
- Wrap the server into a **Dockerized microservice**.
- Build a **streaming simulator** using **Kafka** or **Redpanda** that reads video frames and sends them for inference.
- Log **latency and throughput** metrics and demonstrate correct end-to-end functionality.

---

## ⚙️ Project Breakdown

### 1. Inference Service
- Use a pretrained PyTorch model (e.g., ResNet18).
- Accept images over gRPC and return the top-1 predicted label.
- Preprocess images using OpenCV.

### 2. Docker Microservice
- Build and run the inference service inside Docker.
- Use multi-stage builds for efficiency.
- Include a simple health check or readiness probe endpoint (HTTP/gRPC).

### 3. Streaming Input (Producer/Consumer)
- Simulate streaming using Kafka or Redpanda:
  - Producer reads video or webcam frames and pushes them to a topic.
  - Consumer receives the frames and calls the inference gRPC endpoint.
  - Use serialized images (e.g., JPEG or base64-encoded) in the message payload.

### 4. Performance Logging
- Measure and log:
  - Inference time per frame (latency)
  - Average throughput (frames per second)
- Print summary after running for 30 seconds.

---

## 📝 Submission Guidelines

- Fork or clone this repo (or structure your own).
- Include the following:
  - `/inference_service/` – gRPC server with PyTorch inference
  - `/streaming_simulator/` – Kafka or Redpanda producer/consumer code
  - `Dockerfile` – multi-stage, production-ready image
  - `requirements.txt` or `environment.yml`
  - `README.md` – with setup instructions and how to run tests

- Optional but appreciated:
  - Use TorchScript or ONNX to optimize inference
  - Add a Prometheus metrics endpoint or performance dashboard
  - Include logging to file with timestamps

---

## 🧑‍💻 Bonus (Nice-to-Have)

- GPU/CPU fallback toggles
- Test script to load test the gRPC endpoint

---

## ✅ Evaluation Criteria

| Area              | Weight | Description |
|-------------------|--------|-------------|
| Functionality     | 40%    | End-to-end pipeline works as described |
| Code Quality      | 20%    | Clean, modular, well-documented |
| Docker Usage      | 15%    | Proper image build, health checks, reproducibility |
| Streaming Logic   | 15%    | Correct usage of producer/consumer, data flow |
| Performance Logs  | 10%    | Accurate latency/FPS reporting |

---

Thank you! We look forward to reviewing your submission.  
— Kookree Engineering Team

