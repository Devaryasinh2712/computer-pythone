def lowercase(a):
    d=""
    for i in a :
        if "A"<=i<="Z":
            d+=chr(ord(i)+32)  
        else:
            d+=i
    return d
         
    


def uppercase(a):
    q=""
    for i in a :
        if "a"<=i<="z":
             q+=chr(ord(i)-32)
        else:
            q+=i
    return  q
        

def togglecase(a):
    l=""
    for i in a :
        if "a"<=i<="z":
            l+=chr(ord(i)-32)
        elif "A"<=i<="Z":
            l+=chr(ord(i)+32)
        else:
            l+=i
    return l

a=input("enter a string")
print("upper",uppercase(a))
print("lower",lowercase(a))
print("toggle",togglecase(a))





    

        
    

        
        
        
