from tkinter import *

# create root window
root = Tk()



root.title("hello world")

root.geometry('300x200')

text1 = Label(text = "hello every one")
photo1 = PhotoImage(file="download.png")
photo1_lable= Label(Image=photo1)
photo1_lable.pack()
text1.grid()
Button1= Tk.button(text="count", width=30)

Button1.pack()
root.mainloop()