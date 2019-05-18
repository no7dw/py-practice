import time
def log(fun):
    print('log: ',fun.__name__)
    def wrapped(*args,**kws):
        stime = time.time() 
        retVal = fun(*args,**kws)
        used_time = time.time() - stime 
        print(fun.__name__,' used ' , used_time, 's' , 'para', args,  kws)
        return retVal
    return	wrapped
@log
def service(a, b,c ):
    time.sleep(1)
@log
def service2(a, b, c):
    time.sleep(2)

if __name__ == '__main__':
    service('first', '2', 3)
    service2('second', '2', 3)

