def ddd(num,count,sum=0):
    if count==0:
        return sum
    else:
        temp=int(str(num)*count)
        sum+=temp
        return ddd(num,count-1,sum)

x=ddd(9,3)
print(x)
