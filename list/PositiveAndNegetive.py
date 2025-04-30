import random
l=[]
for i in range(0,30):
    a=random.randint(-100,100)
    l.append(a)

print(l)

l1=[]
l2=[]

for i in l :
    if i>=0 :
        l1.append(i)
    else :
        l2.append(i)

print(l1)
print(l2)
