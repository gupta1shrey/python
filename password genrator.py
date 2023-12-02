import random
q="QWERTYUIOPASDFGHJKLZXCVBNM"
f="qwertyuioplkjhgfdsazxcvbnm"
r="!@#$%^*()_|:;]]][[[{"
n="1234567890"
ry=f+r+q+n
lg=8
password="".join(random.sample(ry,lg))
print(password)