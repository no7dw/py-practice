import requests

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit(url):
    return send_request(url)
