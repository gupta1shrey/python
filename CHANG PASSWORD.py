o="qwerty@123"
def shrey():
    global o
    t=input("enter your user id")

    if t=="guptashrey":
        print("your id is correct")
        c=input("enter password")
    if c==o:
        print("your password is correct") 
    elif c!=o:
        print("your password is wrong")
        
        o=input("change your password")
        
        print("your password secsess fully change")
        shrey()
shrey()
     


