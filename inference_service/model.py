import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import cv2
import numpy as np

model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

imagenet_labels = dict(enumerate(open("imagenet_classes.txt")))

def preprocess_image(image_bytes):
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    return transform(pil_img).unsqueeze(0)

def predict(image_bytes):
    input_tensor = preprocess_image(image_bytes)
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted = torch.max(output, 1)
    return imagenet_labels[predicted.item()].strip()
