class A():
    def run(self, config):
        print('this is A', config)

class B():
    def run(self, config):
        print('this is B', config)

p_d = {
   'A': A,
   'B': B
 }
config1 = {'u':1,'n':'w'}
config2 = {'u':2,'n':'w'}
p_d['A']().run(config1)
p_d['B']().run(config2)

