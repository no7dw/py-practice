import redis   
import time
#import sys
r = redis.Redis(host='localhost', port=6379)   


def get_set():
    r.set('name', 'wade')  
    print(r['name'])
    print(r.get('name'))  
    print(type(r.get('name')))

def sub():
    PAUSE = True
    p = r.pubsub()
    p.subscribe('channel1')
    while PAUSE :
        msg = p.get_message()
        if msg :
            re = time.time()
            cont = msg['data']
            st = float(cont)
            print('sub diff', re-st)

def pub():
    s = time.time() 
    r.publish('channel1', s)
    e = time.time() 
    print("pub diff", e-s) 
    

#if __name__ == '__main__':
#    if(1 == len(sys.argv)):
#        print("usage:\npython3 p.py s \npython3 p.py p")
#    elif ('s' == sys.argv[1]):
#        sub()
#    else:        
#        pub()
    
