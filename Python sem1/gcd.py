def gcd(x,y):
    assert x!=0 or y!=0
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(-24,-4))
