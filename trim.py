import tkinter as tk
from tkinter import filedialog
import pydub

class AudioTrimmer:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Trimmer")

        self.file_path = ""
        self.start_time = 0
        self.end_time = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select audio file to trim:").grid(row=0, column=0, padx=5, pady=5)
        self.file_label = tk.Label(self.master, text="")
        self.file_label.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.select_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.master, text="Start time (in seconds):").grid(row=1, column=0, padx=5, pady=5)
        self.start_entry = tk.Entry(self.master)
        self.start_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.master, text="End time (in seconds):").grid(row=2, column=0, padx=5, pady=5)
        self.end_entry = tk.Entry(self.master)
        self.end_entry.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_file, state=tk.DISABLED)
        self.save_button.grid(row=3, column=1, padx=5, pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        self.file_label.config(text=self.file_path)

    def save_file(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        if save_path:
            trimmed_audio = self.trim_audio()
            trimmed_audio.export(save_path, format="mp3")
            tk.messagebox.showinfo("Success", "Trimmed audio saved successfully.")

    def trim_audio(self):
        audio = pydub.AudioSegment.from_file(self.file_path)
        start_time = int(self.start_entry.get()) * 1000
        end_time = int(self.end_entry.get()) * 1000
        trimmed_audio = audio[start_time:end_time]
        return trimmed_audio

    def validate_input(self):
        if self.file_path == "":
            tk.messagebox.showerror("Error", "Please select an audio file.")
            return False
        if self.start_entry.get() == "" or self.end_entry.get() == "":
            tk.messagebox.showerror("Error", "Please specify start and end time.")
            return False
        if int(self.start_entry.get()) >= int(self.end_entry.get()):
            tk.messagebox.showerror("Error", "End time must be greater than start time.")
            return False
        return True

    def on_entry_changed(self, *args):
        if self.validate_input():
            self.save_button.config(state=tk.NORMAL)
        else:
            self.save_button.config(state=tk.DISABLED)

root = tk.Tk()
app = AudioTrimmer(root)
root.mainloop()
