s ="44.87"
a = float(s)
c=str(a)#str value with point is not directly converted in int value
print(type(a))#so we have to convert it in float value fist
print(type(c))
print(type(s))
d =input("enter your user fist name ")
f =input("enter your user last name ")

g =d+f+"@gmail.com"
print(g)
k ="your email id caracters are "
p =len(g)
o =str(p)
print(k+o)

N = p % 2
if N==0:
    print("your id is secure")
else:
    print("your id is unsecure")