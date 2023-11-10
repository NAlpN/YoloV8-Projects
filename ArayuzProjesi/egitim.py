from ultralytics import YOLO
from PIL import Image

DATA_DIR = 'C:/Users/alpnn/Masaüstü/GitHub/YoloV8-Projects/ArayuzProjesi/ArayuzProjesi/ultralytics/datasets'

#model = YOLO('yolov8n-cls.pt')

#results = model.train(data=DATA_DIR, epochs=10, imgsz=64)

model = YOLO('C:/Users/alpnn/Masaüstü/GitHub/YoloV8-Projects/ArayuzProjesi/ArayuzProjesi/ultralytics/runs/classify/train/weights/best.pt')

im1 = Image.open("P_1.jpg")
model.predict(source=im1, save=True)