import random
l=[]
for i in range(0,5) :
    a=random.randrange(1,100,2)
    l.append(a)
print(l)

l2=[]
for i in range(0,4) :
    b=random.randrange(0,100,2)
    l2.append(b)
print(l2)

t=2
for i in l2 :
    l.insert(t,i)
    t=t+1

print("After inserting : ")
print(l)

l.sort()
print("The sorted list is : ",l)






