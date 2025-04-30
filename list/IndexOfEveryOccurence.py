import random
l=[]
for i in range(0,20):
    a=random.randint(0,19)
    l.append(a)
print(l)

b=int(input("Enter a number : "))

for i,j in enumerate(l) :
    if j==b :
        print(i)
        
    
    
