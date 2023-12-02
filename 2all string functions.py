from math import comb
# type casting variable 
r=int(2.1)
g=float(22.3)
f=str(22)
print(type(r))
print(type(g))
print(type(f))
H="MY  favoirite colour IS red"    
print(H[:7])#slice using ending range
print(H[3:10])#slice using starting and starting range
print(H[10:])#slie using starting range
print(H[-19:-12])#sclice using negetive 
#convert string into upper case
print(H.upper()) # convert into upper case 
print(H.lower()) #convert into lower case 
y="  a  sia  sd  "
print(y.strip())
print("whatis your favoirite colour?")
#remove extra spaces
v=input("")
print(H.replace("shrey",v))
H="your favarit, colour IS shrey"  
print(H.split(","))
f="hohhhhhhhooooooooooooooooooooooooooooooooooooooooolla"
print(f.capitalize())#
print(f.title())
print(f.swapcase())
print(f.center(10))
print(f.count("o"))
print(f.endswith(","))
 
