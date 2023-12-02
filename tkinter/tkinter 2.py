

import tkinter as tk 
r = tk.Tk()
r.geometry('300x200')
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 

r.mainloop() 