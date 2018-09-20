def gcd(a,b):
    # if b > a:
    #     if b/a == 0:
    #         return a
    #     else:
    #         return gcd(b/a,a)
    # else:
    #     if a/b == 0:
    #         return b 
    #     else:
    #         return gcd(b,a/b)
    
    q = a/b
    if q == 0:
        print(b)
    else:
        a = b
        b = q
    return gcd(a,b)
print(gcd(5,4))




