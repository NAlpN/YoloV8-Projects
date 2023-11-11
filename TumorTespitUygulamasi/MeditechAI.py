import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

class YOLOv8Interface:
    def __init__(self, master):
        self.master = master
        master.title("YOLOv8 Arayüzü")

        master.geometry("800x600")

        master.configure(bg="#1F424B")

        self.label_ata_ait = tk.Label(master, text="Meditech AI", font=("Helvetica", 24), bg="#1F424B", fg="#FFFFFF")
        self.label_ata_ait.pack(pady=20)

        self.select_button = tk.Button(master, text="Görüntü Gir", command=self.select_image, width=20, height=3)
        self.select_button.pack(pady=10)

        self.predict_button = tk.Button(master, text="Neyim Var?", command=self.predict_image, width=20, height=3)
        self.predict_button.pack(pady=10)

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        # Model yolunu gir
        self.model_path = "C:/Users/alpnn/Masaüstü/Python Dosyaları/ultralytics/runs/classify/train3/weights/best.pt"


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
        image = self.image.resize((600, 400))
        photo = ImageTk.PhotoImage(image=image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

def main():
    root = tk.Tk()
    app = YOLOv8Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
