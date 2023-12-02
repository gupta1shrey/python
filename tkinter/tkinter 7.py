from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk

base = tk.Tk()
base.title("hello")
base.geometry("600x700")
f1 = Frame(base, bg="red", borderwidth=10, relief=SUNKEN)
f1.pack(side=RIGHT, fill="y")

f2 = Frame(base, bg="red", borderwidth=10, relief=SUNKEN)
f2.pack(side=LEFT, fill="y")

f3 = Frame(base, bg="red", borderwidth=10, relief=SUNKEN)
f3.pack(side=TOP, fill="y")

l = tk.Button(f1, text="hello every one", width=25)
l.pack(side=RIGHT)

l2 = tk.Button(f2, text="hello every one", width=25)
l2.pack(side=LEFT)

l3 = tk.Button(f3, text="hello every one", width=25)
l3.pack(side=TOP)

base.mainloop()