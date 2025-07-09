from concurrent import futures
import grpc
import streaming_simulator.inference_pb2_grpc as inference_pb2_grpc
import streaming_simulator.inference_pb2 as inference_pb2
from model import predict

class InferenceServiceServicer(inference_pb2_grpc.InferenceServiceServicer):
    def Predict(self, request, context):
        label = predict(request.image)
        return inference_pb2.PredictionResponse(label=label)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    inference_pb2_grpc.add_InferenceServiceServicer_to_server(InferenceServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
