import tkinter as tk
from threading import Thread
import time

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.root.geometry("600x400")  # Set the window size to 600x400

        self.label = tk.Label(self.root, text="Enter time in seconds:", font=('Helvetica', 24), fg='blue')
        self.label.pack()

        self.entry = tk.Entry(self.root, font=('Helvetica', 24), width=20)
        self.entry.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer, font=('Helvetica', 24), fg='green')
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_timer, font=('Helvetica', 24), fg='red', state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(self.button_frame, text="Resume", command=self.resume_timer, font=('Helvetica', 24), fg='green', state=tk.DISABLED)
        self.resume_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer, font=('Helvetica', 24), fg='orange', state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT)

        self.time_label = tk.Label(self.root, text="", font=('Helvetica', 48), fg='blue')
        self.time_label.pack()

        self.running = False
        self.count = 0
        self.stop_thread = False
        self.paused = False
        self.thread = None

    def countdown(self, count):
        self.running = True
        while count > 0 and not self.stop_thread:
            mins, secs = divmod(count, 60)
            self.time_label.config(text=f"{mins:02d}:{secs:02d}")
            self.root.update()
            time.sleep(1)
            count -= 1
            while self.paused:
                time.sleep(0.1)
        if not self.stop_thread:
            self.time_label.config(text="Time's up!")
        self.running = False

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.resume_button.config(state="disabled")
        self.reset_button.config(state="normal")
        self.count = int(self.entry.get())
        self.stop_thread = False
        self.paused = False
        self.thread = Thread(target=self.countdown, args=(self.count,))
        self.thread.start()

    def stop_timer(self):
        self.stop_thread = True
        self.paused = True
        self.resume_button.config(state="normal")

    def resume_timer(self):
        self.paused = False
        self.stop_thread = False
        self.resume_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def reset_timer(self):
        self.stop_thread = True
        self.paused = False
        self.time_label.config(text="")
        self.entry.delete(0, tk.END)
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.resume_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    timer = CountdownTimer()
    timer.run()