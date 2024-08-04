import qrcode
import tkinter as tk
class QREncoder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("QR Code Encoder")

        # Create input field for data
        self.data_label = tk.Label(self.window, text="Enter data (URL or text):")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.window)
        self.data_entry.pack()

        # Create button to generate QR code
        self.generate_button = tk.Button(self.window, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        # Create label to display QR code
        self.qr_code_label = tk.Label(self.window, text="")
        self.qr_code_label.pack()

    def generate_qr_code(self):
        data = self.data_entry.get()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save("qr_code.png")

        self.qr_code_label.config(text="QR Code generated successfully!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    encoder = QREncoder()
    encoder.run()