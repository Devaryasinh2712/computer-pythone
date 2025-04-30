a=input("enter 1st string")
b=input("enter 2nd string")
found=False
p=len(a)
q=len(b)
for i in range(p-q+1):
    match=True
    for j in range(q):
        if a[i+j]!=b[j]:
            match=False
            break
        elif b[i+j]!=a[j]:
            match=False
        
    if match:
        found=True
        break
if found:
    print("substring")
else:
    print("not found")
