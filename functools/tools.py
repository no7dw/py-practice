# py 3.4 
# singledispatch 用一个单一参数的类似去实现重载

from functools import singledispatch 

@singledispatch
def fun(numbers):
  print('parameter is string')

@fun.register(int)
# @fun.register(Decimal)
@fun.register(float)
def test_generic_1(numbers):
  print('parameter is numbers')

@fun.register(list)
def test_generic_1(numbers):  
  print('parameter is list')

# the following won't work
# @singledispatch
# def fun2(numbers, Value):
#   print('parameter is 2 str')

# @fun2.register(int , int)
# def test_generic_1(n1,n2):  
#   print('parameter is str')

# def test_generic_1(numbers):  
#   print('parameter is dict')  

@singledispatch
def fun3(numbers, second_value):
  print('fun3 parameter is string')

@fun3.register(int)
@fun3.register(float)
def test_generic_1(numbers, second_value):
  print('fun3 parameter is numbers')

@fun3.register(list)
def test_generic_1(numbers, second_value):  
  print('fun3 parameter is list')

if __name__ == "__main__":
  fun(8888)
  fun(88.88)
  fun([8,8,8,8])
  fun("8888")
  # fun2("12","23")
  # fun2(12, 23)
  fun3(8888, 123)
  fun3(88.88, 123)
  fun3([8,8,8,8], 123)
  fun3("8888", 123)