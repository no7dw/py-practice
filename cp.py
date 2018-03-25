import copy
print("python is pass by reference")
a=[[1],[2],[3]]
b=copy.copy(a)
c=copy.deepcopy(a) # I would not change if a change

print("before","==>")
print("a",a)
print("b",b)
print("c",c)
###mod

a[0][0]=0
a[1]=None
#a[1][0]=None

print("after","==>")
print("a",a)
print("b",b)
print("c",c)
