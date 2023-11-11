from ultralytics import YOLO
from PIL import Image

DATA_DIR = 'C:/Users/alpnn/Masaüstü/Python Dosyaları/ultralytics/datasets'

model = YOLO('yolov8x-cls.pt')

results = model.train(data=DATA_DIR, epochs=10, imgsz=64)