from gevent import monkey; monkey.patch_all() #in fact it's slower than socket-test.py # monkey.patch_all()
import gevent
from  urllib  import request
import datetime

def read_web(url):
    if url.find("https://"):
        url = "https://" + url 
    print('open' , url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    return len(data)

s = datetime.datetime.now()
urls = ['www.youtube.com', 'www.jd.com', 'www.google.com', 'www.qq.com']
jobs = [gevent.spawn(read_web, url) for url in urls]
gevent.joinall(jobs, timeout=15)
e= datetime.datetime.now()
print(e-s)
print([job.value for job in jobs])