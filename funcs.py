#List of functions that will help me with my other files.
from tkinter import *
from tkinter import messagebox

def center_window(root, size):
    """Take size string and center the window onto the screen"""
    win_size = size.split("x")

    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    win_x = int((screen_width/2) - (int(win_size[0])/2))
    win_y = int((screen_height/2) - (int(win_size[1])/2))

    root.geometry("{0}+{1}+{2}".format(size, win_x, win_y))

def create_window(root, title, color):
    root.title(title)
    root.configure(background=color)

def errorBox(message):
    messagebox.showerror("ERROR", message)