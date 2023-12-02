from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.title("Yuniek's Newspaper")
base.geometry("1180x644")
base.minsize(width=300, height=300)

# Header for newspapaer
Header = Frame(base, bg="grey", borderwidth=5, relief=SUNKEN, pady=25)
Header.pack(side=TOP, fill=X)
t = Label(Header, text="Yuniek's Newspaper", bg="grey", font="Arial 19 bold italic")
t.pack()

# News 1
f1 = Frame(base, bg="lightblue", borderwidth="5", relief=SUNKEN, pady=25)
f1.pack(fill=X, anchor='nw')

p1 = Image.open("1.jpg")
P1 = ImageTk.PhotoImage(p1)

l1 = Label(f1, image=P1, width=130, height=130)
l1.pack(side=LEFT)
l12 = Label(f1, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l12.pack()



base.mainloop()