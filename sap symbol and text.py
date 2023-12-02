u="!@#$%^&*()_+><\|\;/.,=-:"
e=input("enter your name")
r=""
o=""
for x in e:
    if x in u:
        o=o+x
    else:
        r=r+x
print(r)
print(o)