from ultralytics import YOLO
#from PIL import Image

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# ic_image = Image.open("indir.jpg")
# sonuc = model.predict(source=ic_image, save = True)

sonuc = model.predict(source="0")     # 0 webcam için

#sonuc = model.predict(source="PredictionVideo/Siha.mp4", show=True, save = True<)