from tkinter import *
import tkinter as tk
r = tk.Tk()
r.geometry('4000x3000') 
w =Label(text="i am shrey and this is mt fist gui", padx=100, pady=100, width=100, bg="black", fg="white").grid(row=1)
button = tk.Button(r, text='Stop', padx=10, pady=20, width=25, command=r.destroy, bg='black', fg='white', bd=21, font='Helvetica').grid(row=3)



Label(r, text='First Name').grid(row=0) 
Label(r, text='Last Name').grid(row=14) 
e1 = Entry(r) 
e2 = Entry(r) 
e1.grid(row=0, column=1) 
e2.grid(row=14, column=1) 
mainloop() 