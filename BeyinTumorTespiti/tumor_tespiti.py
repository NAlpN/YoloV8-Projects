from roboflow import Roboflow
rf = Roboflow(api_key="EAACtPRrcBp3KImKcGqJ")
project = rf.workspace().project("beyin_tumor")
model = project.version(1).model

# infer on a local image
#print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
#model.predict("normal/N_50.jpg", confidence=40, overlap=30).save("prediction.jpg")
model.predict("glioma_tumor/G_30.jpg", confidence=40, overlap=30).save("prediction2.jpg")
model.predict("meningioma_tumor/M_30.jpg", confidence=40, overlap=30).save("prediction3.jpg")
#model.predict("pituitary_tumor/P_50.jpg", confidence=40, overlap=30).save("prediction4.jpg")


# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())