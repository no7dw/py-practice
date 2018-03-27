import time
def log(fun):
    print('log: ',fun.__name__)
    def wrapped(*args,**kws):
        stime = time.time() 
        retVal = fun(*args,**kws)
        used_time = time.time() - stime 
        print(fun.__name__,' used ' , used_time, 's')
        return retVal
    return	wrapped
@log
def service(para):
    time.sleep(1)
@log
def service2(para):
    time.sleep(2)

if __name__ == '__main__':
    service('first')
    service2('second')

