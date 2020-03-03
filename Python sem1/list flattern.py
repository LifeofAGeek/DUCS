def ListFlattern(lst,index=0,new=[]):
    if index==len(lst):
        return 
    else:
        l=lst[index]
        if type(l)==list:
            ListFlattern(l,0,new)
            index+=1
            ListFlattern(lst,index,new)
        else:
            index+=1
            new.append(l)
            ListFlattern(lst,index,new)
        return new

new=ListFlattern([3,[1,2],[1,2,3,4],[3,4,5,6,7])
print(new)
