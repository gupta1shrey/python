
e = int(input("enter a number"))
v = 0 

for i in range(1,e+1):
    r=e%i
    if r == 0:
        v+= 1
    


if v == 2:
    print("it is a prime number")
else:
    print("it is a non prime number") 