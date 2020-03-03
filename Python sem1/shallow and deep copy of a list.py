def ShallowCopy1(lst,index=0,newList=[]):
  '''
  objective: Copy a list to another list without using any pre-defind functions
  Input: lst, index, newList
  output: Returns a new copied list
  approach: recursion
  '''
  if index==len(lst):
    return newList
  else:
    newList+=[lst[index]]
    return ShallowCopy1(lst,index+1,newList)
    
def Shallowcopy2(lst,index=0,newList=[]):
  '''
  objective: Copy a list to another list using append function
  Input: lst, index, newList
  output: Returns a new copied list
  approach: recursion

  '''
  if index==len(lst):
    return newList
  else:
    newList.append(lst[index])
    return ShallowCopy2(lst,index+1,newList)
    
def DeepCopy(lst,newList=[],index=0):
  '''
  objective: Copy a list to another list by creating instance of every nested list
  Input: lst, index, newList
  output: Returns a new copied list
  approach: recursion

  '''
  if index==len(lst):
    return newList

  else:

    if type(lst[index])!=list:
      newList.append(lst[index])
      return DeepCopy(lst,newList,index+1)
      
    else:
      x=lst[index]
      nested=[]
      DeepCopy(x,nested,0)
      newList.append(nested)
      return DeepCopy(lst,newList,index+1)
        
