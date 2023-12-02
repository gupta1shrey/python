def djg():
    t=input("enter your email id")
    w,u=t.split("@")

    if u=="gmail.com":
        print("your id is fully correct")
    else :
        print("plese re enter your id")
    djg()
djg()
