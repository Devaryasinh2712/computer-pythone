import random
l=[]
for i in range(0,50):
    a=random.randint(1,30)
    l.append(a)

print(l)
print()

for i in l :
    t=l.count(i)
    if t>1 :
        for j in range(1,t) :
            l.remove(i)

print(l)
