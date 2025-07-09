FROM python:3.9-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS build

COPY . .

WORKDIR /app/inference_service
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inference.proto

CMD ["python", "server.py"]
