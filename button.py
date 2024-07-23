from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog as fd

from os import path

paths = []

def warning_not_path(line):
    root = Tk()
    root.withdraw()  
    messagebox.showwarning("Caution", "I did not find the file at " + line + ". Please check the file path.")

def show(listbox):
    listbox.delete(0, END)
    for path in paths:
        listbox.insert(END, path)
    # print(paths)


def add(listbox, Path):
    line = Path.get()
    line = line.strip("\n").strip("\"")
    if path.isfile(line):
        if line:
            paths.append(line)
            show(listbox)
    else:
        warning_not_path(line)
    Path.set("")
        


def deleteAll(listbox):
    listbox.delete(0, END)
    paths.clear()
    show(listbox)


def delete(listbox):
    if paths:
        listbox.delete(END)
        paths.pop()
        show(listbox)