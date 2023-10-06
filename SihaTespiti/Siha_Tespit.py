from roboflow import Roboflow
rf = Roboflow(api_key="EAACtPRrcBp3KImKcGqJ")
project = rf.workspace().project("siha_etiketleme")
model = project.version(1).model

# infer on a local image
#print(model.predict("dataset/1 (30).jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("dataset/1 (44).jpg", confidence=40, overlap=30).save("prediction44.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())