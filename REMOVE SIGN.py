p="!@#$%^&*()_+|:?><?>,;'[]\=-"#remove puntuations from string
t=input("enter your name")
n=""
for a in t:
    if a not in p:
        n=n+a

print(n)