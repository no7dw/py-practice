import copy
print("python is pass by reference")
a=[[1],[2],[3]]
b=copy.copy(a) # copy 简单对象
c=copy.deepcopy(a) # I would not change if a change copy 复杂子对象(object)

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

[ref link](https://iaman.actor/blog/2016/04/17/copy-in-python)