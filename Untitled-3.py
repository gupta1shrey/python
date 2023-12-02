


name =input("enter your name ")
age =input("enter your age ")

m1 =int(input("enter your math marks(out of 80)"))
m2 =int(input("enter your science marks(out of 80)"))
m3 =int(input("enter your hindi marks(out of 80)"))
m4 =int(input("enter your english marks(out of 80)"))
m5 =int(input("enter your sanskrit marks(out of 80)"))
m6 =int(input("enter your social science marks(out of 80)"))
m7 =int(input("enter your ai marks(out of 80)"))

total =m1+m2+m3+m4+m5+m6+m7
percentage=float(total)*(100/560)
print("your name is "+name)
print("your age is " + age )
print("your percentage is ",percentage)

if total < 168 :
    print("you are fail")
else :
    print("you are pass")

