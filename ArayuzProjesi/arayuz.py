import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

class YOLOv8Interface:
    def __init__(self, master):
        self.master = master
        master.title("YOLOv8 Arayüzü")

        master.geometry("600x400")

        self.select_button = tk.Button(master, text="Resim Seç", command=self.select_image, width=20, height=2)
        self.select_button.pack(pady=10)

        self.predict_button = tk.Button(master, text="Tahmin Yap", command=self.predict_image, width=20, height=2)
        self.predict_button.pack(pady=10)

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        self.model_path = "C:/Users/alpnn/Masaüstü/GitHub/YoloV8-Projects/ArayuzProjesi/ArayuzProjesi/ultralytics/runs/classify/train/weights/best.pt"

        self.model = YOLO(self.model_path)

        self.selected_image_path = None

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_image_path = file_path
            self.image = Image.open(file_path)
            self.display_image()

    def predict_image(self):
        if self.selected_image_path:
            # Kullanıcının seçtiği fotoğrafı al
            selected_image = Image.open(self.selected_image_path)

            # YOLOv8 modelini kullanarak resimdeki nesneleri tahmin et
            results = self.model.predict(source=selected_image, show=True)

        else:
            print("Lütfen önce bir resim seçin.")

    def display_image(self):
        image = self.image.resize((400, 300))
        photo = ImageTk.PhotoImage(image=image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

def main():
    root = tk.Tk()
    app = YOLOv8Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
