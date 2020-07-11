import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


def submit_tiling(window, tiling_pattern):
    # window.destroy()
    process_submission(tiling_pattern)


def invalid_input():
    messagebox.showerror("Error", "Invalid Input")


edge_color_re = "^(\w*)-(#[0-9A-F]{6})$"
tile_re = "^(\w*):(\w*),(\w*),(\w*),(\w*)$"
seed_re = "^(\w*)$"

def process_submission(sub):
    sub = sub.split('\n')
    # print(sub)
    edgelist = {}
    tilelist = {}
    state = 0
    for i in sub:
        if (state == 0):
            ver = re.search(edge_color_re, i)
            if (ver):
                edgelist[ver.group(1)] = ver.group(2)
                state = 1
            else:
                invalid_input()
                state = -1
        elif (state == 1):
            ver = re.search(edge_color_re, i)
            if (ver and not ver.group(1) in edgelist):
                edgelist[ver.group(1)] = ver.group(2)
            else:
                ver = re.search(tile_re, i)
                if (ver):
                    tilelist[ver.group(1)] = [ver.group(
                        2), ver.group(3), ver.group(4), ver.group(5)]
                    state = 2
                else:
                    invalid_input()
                    state = -1
        elif (state == 2):
            ver = re.search(tile_re, i)
            if (ver and not ver.group(1) in tilelist):
                tilelist[ver.group(1)] = [ver.group(
                    2), ver.group(3), ver.group(4), ver.group(5)]
            else:
                ver = re.search(seed_re, i)
                if (ver):
                    seed = ver.group(0)
                    state = 3
                else:
                    invalid_input()
                    state = -1
        elif (state == 3):
            if (i):
                invalid_input()
                state = -1
        else:
            break

    if (state == 3):
        print(tilelist)
        print(edgelist)
        print(seed)
        # print("fuck")
    else:
        print("Invalid Input")

def get_tileset():
    window = tk.Tk()
    window.geometry("900x400")
    L1 = Label(window, text="Enter your tiling pattern")
    L1.pack(side=LEFT)
    S = ScrolledText(window)
    S.pack(side=LEFT)
    B = tk.Button(window, text="Ok", command=lambda: submit_tiling(
        window, S.get('1.0', END)))
    B.pack(side=LEFT)
    window.mainloop()

get_tileset()