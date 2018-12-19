import http.client

def read_web(url):
  con = http.client.HTTPSConnection(url, 443)
  con.request('GET', '/')
  res = con.getresponse()
  res_arr = []
  while not res.closed:
    res_arr.append(res.read(200))
  return res_arr

if __name__ == "__main__":
  read_web('https://www.baidu.com')