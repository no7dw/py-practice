class Base(object):
    def __init__(self):
        pass
    def run(self):
        print("base run")

class Third(Base):
    def __init__(self):
        pass
    def run(self):
        print("third run")

if __name__ == "__main__":
    b = Base() 
    b.run()
    t = Third()
    t.run()
