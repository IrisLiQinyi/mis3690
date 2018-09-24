def gcd(a,b):
    print ('Current a,b',a,b)  
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
    
print(gcd(1245,837))




