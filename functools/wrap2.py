
def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print ('before call')
        return func(*args, **kwargs)
    return call_it

# 仅仅是注解
@wrap
def hello():
    """say hello"""
    print('hello world')


if __name__ == '__main__':
    hello()
    print(hello.__name__) # call_it ，错误的
    print(hello.__doc__)  # wrap func: call_it
  