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
            print("receive",time.time()) 
            cont = msg['data']

def pub():
    s = time.time() 
    print("before publish",s) 
    #r.publish('channel1','helloworld')
    r.publish('channel1', s)
    e = time.time() 
    print("after publish", e) 
    print("diff", e-s) 
    

if __name__ == '__main__':
    #sub()
    pub()
    
