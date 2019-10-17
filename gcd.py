'''def gcd(x,y):
    assert x!=0 or y!=0
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(-24,-4))'''
l=[1,2,3,4,[1,2]]
n=[]
for i in range(0,len(l)):
     n+=[l[i]]
print(n)