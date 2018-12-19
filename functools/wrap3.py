from functools import update_wrapper

def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print('before call')
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print('hello world2')

if __name__ == '__main__':
    hello2()
    print(hello2.__name__) # wrap 带过去 __name__、module、__doc__和 __dict__ ，因此正常显示
    print(hello2.__doc__) 