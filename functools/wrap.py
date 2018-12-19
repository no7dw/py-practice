from functools import wraps
def wrap3(func):
    # @wraps(func)
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print ('before call')
        return func(*args, **kwargs)
    return call_it

@wrap3
def hello3():
    """test hello 3"""
    print ('hello world3')

if __name__ == "__main__":
    hello3()