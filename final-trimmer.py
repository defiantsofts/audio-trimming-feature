from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment

# Function to create a new audio file with the selected range
def create_new_file():
    # Get the values entered by the user
    file_path = file_path_entry.get()
    start_min = int(start_min_entry.get())
    start_sec = int(start_sec_entry.get())
    end_min = int(end_min_entry.get())
    end_sec = int(end_sec_entry.get())

    # Open the selected file
    song = AudioSegment.from_file(file_path, format="mp3")

    # Calculate the start and end times in milliseconds
    start = ((start_min * 60) + start_sec) * 1000
    end = ((end_min * 60) + end_sec) * 1000

    # Extract the selected range from the song
    clip = song[start:end]

    # Ask the user to select a save location and filename
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3")

    # Save the extracted clip as a new mp3 file
    clip.export(save_path, format="mp3")

    # Show a message to indicate that the new file has been created
    status_label.config(text="New Audio file is created and saved")

# Create the main window
root = Tk()
root.title("Audio Clipper")

# Create a frame to hold the file path input field and browse button
file_frame = Frame(root)
file_frame.pack(pady=10)

file_path_label = Label(file_frame, text="File Path:")
file_path_label.pack(side=LEFT)

file_path_entry = Entry(file_frame, width=50)
file_path_entry.pack(side=LEFT, padx=10)

browse_button = Button(file_frame, text="Browse", command=lambda: file_path_entry.insert(0, filedialog.askopenfilename()))
browse_button.pack(side=LEFT)

# Create a frame to hold the start/end time input fields
time_frame = Frame(root)
time_frame.pack()

start_label = Label(time_frame, text="Start Time (mm:ss):")
start_label.pack(side=LEFT)

start_min_entry = Entry(time_frame, width=2)
start_min_entry.insert(END, "1")
start_min_entry.pack(side=LEFT)

start_colon_label = Label(time_frame, text=":")
start_colon_label.pack(side=LEFT)

start_sec_entry = Entry(time_frame, width=2)
start_sec_entry.insert(END, "10")
start_sec_entry.pack(side=LEFT)

end_label = Label(time_frame, text="End Time (mm:ss):")
end_label.pack(side=LEFT)

end_min_entry = Entry(time_frame, width=2)
end_min_entry.insert(END, "2")
end_min_entry.pack(side=LEFT)

end_colon_label = Label(time_frame, text=":")
end_colon_label.pack(side=LEFT)

end_sec_entry = Entry(time_frame, width=2)
end_sec_entry.insert(END, "5")
end_sec_entry.pack(side=LEFT)

# Create a button to initiate the audio extraction
extract_button = Button(root, text="Create Audio Clip", command=create_new_file)
extract_button.pack(pady=10)

# Create a label to show the status of the extraction process
status_label = Label(root, text="", fg="green")
status_label.pack()

root.mainloop()