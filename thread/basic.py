import time,threading
def sleep_loop():
    print("thread is running", threading.current_thread().name)
    count = 0
    while count<4:
        count = count+1
        print("thread working", count)
        time.sleep(1) 

    print("worker finish")

t  = threading.Thread(target=sleep_loop, name='sleep_loop')
t.start()
print("main thread continue")
print("waiting for  thread end")
t.join()
print("main thread end", threading.current_thread().name)

