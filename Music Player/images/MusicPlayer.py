# https://stackoverflow.com/questions/53799070/how-can-i-read-a-file-as-relative-path-in-python-with-visual-studio-code

import os
import tkinter as tk
from tkinter.constants import HORIZONTAL, LEFT, RAISED, SUNKEN, BOTTOM, TRUE, W, X
from tkinter import filedialog
import tkinter.messagebox
from PIL import ImageTk, Image
from pygame import mixer


def play_btn():
    try:
        paused  # Is paused var initiailized?
    except NameError:
        try:  # If paused not initialized then execute this
            music_path = os.path.join(resource_path + "\journey.wav")
            # print('Play: ' + str(os.path.exists(music_path)) + ' - ' + music_path)
            mixer.music.load(filename)  # music_path)
            # mixer.music.load(filename)
            mixer.music.play()
            statusbar["text"] = "Playing: " + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror("Music Player", "File not found")
            print("File not found")
    else:  # If paused is initialized then execute this code
        mixer.music.unpause()


def pause_btn():
    global paused  # Set paused so play function starts where it was paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Paused."


def stop_btn():
    mixer.music.stop()
    statusbar["text"] = "Stopped."


# 'val' is the system variable passed from the scale
def set_vol(val):
    volume = int(val) / 100  # convert slider value (integer to mixer value (decimal)
    mixer.music.set_volume(volume)


def about_us():
    # tk. is not required here
    tkinter.messagebox.showinfo(
        "Music Player", "This is the about info"
    )  # showinfo, showerror, showwarning


def select_file():
    global filename
    filename = filedialog.askopenfilename()
    print("Selected file: " + filename)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

subMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=select_file)
subMenu.add_command(label="Exit", command=root.destroy)

subMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About", command=about_us)


mixer.init()

resource_path = os.path.join(os.getcwd() + "\Music Player\image")
root.title("Music Player")
root.iconbitmap(resource_path + "\\thinking.ico")
root.geometry("300x300")

text = tk.Label(root, text="Music Player")
text.pack(padx=6, pady=10)

# Button frame
middleframe = tk.Frame(root, relief=RAISED, borderwidth=4)
middleframe.pack()

playPhoto = ImageTk.PhotoImage(Image.open(resource_path + "\play.png"))
playBtn = tk.Button(middleframe, image=playPhoto, command=play_btn)
playBtn.pack(side=LEFT, padx=6)
stopPhoto = ImageTk.PhotoImage(Image.open(resource_path + "\stop.png"))
stopBtn = tk.Button(middleframe, image=stopPhoto, command=stop_btn)
stopBtn.pack(side=LEFT, padx=6)
pausePhoto = ImageTk.PhotoImage(Image.open(resource_path + "\pause.png"))
pauseBtn = tk.Button(middleframe, image=pausePhoto, command=pause_btn)
pauseBtn.pack(side=LEFT, padx=6)

scale = tk.Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(60)
mixer.music.set_volume(0.6)
scale.pack()

statusbar = tk.Label(root, text="Welcome.", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
