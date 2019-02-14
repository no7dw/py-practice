import sys
import p
if __name__ == '__main__':
    if(1 == len(sys.argv)):
        print("usage:\npython3 p.py s \npython3 p.py p")
    elif ('s' == sys.argv[1]):
        p.sub()
    else:
        p.pub()
