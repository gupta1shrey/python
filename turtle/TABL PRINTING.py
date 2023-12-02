d=[2,2,2,2,2,2,2,2,2,2,2]
s=1
for x in d:

    print(x*s)
    s=s+1
    if s==10:
        print("table of three")
        a=[3,3,3,3,3,3,3,3,3,3]
        c=1
        for x in a:

          print(x*c)
          c=c+1        
        break