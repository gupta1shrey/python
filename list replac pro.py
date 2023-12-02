 

from operator import index


ame =["savitri gupta", "mohit gupta", "vandana gupta", "sarthak gupta", "shrey gupta"]
 
for x in ame:
    print(x)
    v=ame.index(x)
    c =input("")
    ame[v]= c
    print(ame)
