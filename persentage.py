print("clculate percentage")
i=input("name of student")

r=int(input("total maks"))
s=int(input("enter your maks osf 1st subject"))
if 0<s>25:
    print("you type wrong marks because your marks are mare than 25")
    x=input("reenter your marks")
    s==x
 
h=int(input("enter your maks osf 2nd subject"))
if 0<h>25:
    print("you type wrong marks because your marks are mare than 25")
    q=input("reenter your marks")
    h==q
j=int(input("enter your maks osf 3rd subject"))
if 0<j>25:
    print("you type wrong marks because your marks are mare than 25")
    l=input("reenter your marks")
    j==l
n=int(input("enter your maks osf 4th subject"))
if 0<n>25:
    print("you type wrong marks because your marks are mare than 5")
    o=input("reenter your marks")
    n==o
t=s+h+j+n

print(t)
e=s+h+j+n/r*100
print(e)
if e>=80:
    print("you score grade a")
elif e>=60:
    print("you score grade b")
elif e>=40:
    print("you score grade c")
else:
    print("you are fail")
print("name of studet = "+i)
print("total marks of studet = "+str(t))
print("total percentage of studet = "+str(e))

