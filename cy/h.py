# cython: language_level=3
def say_hello_to(name):
    print("Hello %s!" % name)
if __name__ == '__main__':
    say_hello_to("wade")
