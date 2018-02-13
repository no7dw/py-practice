from urllib import request

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('status code:', f.status)
    print('data:', data.decode('utf-8'))
