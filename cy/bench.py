# cython: language_level=3
import math
import time

def f():
    time1 = time.time()
    for i in range(100000000):
        x = math.sqrt(i)
    time2 = time.time()
    print(time2 - time1)

if __name__ == "__main__":
    f()
