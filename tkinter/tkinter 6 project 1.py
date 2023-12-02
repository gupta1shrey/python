
import tkinter as tk 
r = tk.Tk()

tk.Label(r, text='First Name').grid(row=0) 
tk.Label(r, text='Last Name').grid(row=1) 
e1 = tk.Entry(r) 
e2 = tk.Entry(r) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

button = tk.Button(r, text='Stop', width=25)

button.grid(row=2) 


Lb = tk.Listbox(r) 
Lb.insert(1, 'Python') 
Lb.insert(2, 'Java') 
Lb.insert(3, 'C++') 
Lb.insert(4, 'Any other') 

Lb.grid(row=3)

r.mainloop() 