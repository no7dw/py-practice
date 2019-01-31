import redis   
import time
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
            print("receive", re) 
            cont = msg['data']
            print(cont)
            st = float(cont)
            print('diff', re-st)

def pub():
    print("before publish",time.time()) 
    r.publish('channel1','helloworld')
    print("after publish",time.time()) 
    

if __name__ == '__main__':
    sub()
    #pub()
    
