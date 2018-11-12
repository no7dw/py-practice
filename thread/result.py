# 
# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python

import time,threading
import queue
q = queue.Queue()
def sleep_loop(sec, strarg):
    print("thread is running", threading.current_thread().name,sec, strarg)
    count = 0
    while count< sec**2:
        count = count+1
        print("thread working", count)
        time.sleep(0.1) 
    result = count
    q.put({"name":threading.current_thread().name, "val":result}) 
    print("worker %s finish" % ( threading.current_thread().name))

#t  = threading.Thread(target=sleep_loop, name='sleep_loop', args=2)
t  = threading.Thread(target=sleep_loop, args=(2, "abcdefg",))
t2  = threading.Thread(target=sleep_loop, args=(3, "abcdefg",))
t.start()
t2.start()
print("main thread continue")
print("waiting for  thread end")
t.join()
t2.join()
while not q.empty():
    print('result', q.get())

print("main thread end", threading.current_thread().name)

