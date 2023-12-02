from tkinter import *
import tkinter as tk
r = tk.Tk()
r.geometry("400x400")
pane = Frame(r)
pane.pack(fill = BOTH, expand = True)

b1 = Button(pane, text = "Click me !", 
            background = "red", fg = "white", bd=20)
b1.pack()
b2 = Button(pane, text = "Click me 1!", 
            background = "green", fg = "white", bd=20)
b2.pack()
b3 = Button(pane, text = "Click me 2!", 
            background = "white", fg = "white", bd=20)
b3.pack()

r.mainloop()