a=input("enter a string")
c=0
v="aeiouAEIOU"
for i in a:
    if i in v:
        c+=1
print("number of vowels",c)

