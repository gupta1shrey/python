from tkinter import *
import tkinter as tk
r = tk.Tk()
r.geometry('4000x3000') 
hollo =tk.Label(text="i am shrey and this is mt fist gui", padx=113, pady=94, bg="black", fg="white").grid(row=1)

hollo.pack(anchor ="nw")
r.mainloop()