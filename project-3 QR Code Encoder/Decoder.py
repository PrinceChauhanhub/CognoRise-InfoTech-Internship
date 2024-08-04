import cv2
import pyzbar.pyzbar as pyzbar
import tkinter as tk
from tkinter import filedialog

class QRDecoder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("QR Code Decoder")

        # Create button to select QR code image
        self.select_button = tk.Button(self.window, text="Select QR Code Image", command=self.select_image)
        self.select_button.pack()

        # Create label to display decoded data
        self.decoded_label = tk.Label(self.window, text="")
        self.decoded_label.pack()

    def select_image(self):
        image_path = filedialog.askopenfilename()
        image = cv2.imread(image_path)
        decoded_objects = pyzbar.decode(image)

        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            self.decoded_label.config(text=f"Decoded data: {data}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    decoder = QRDecoder()
    decoder.run()