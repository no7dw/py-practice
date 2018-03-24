from pyknow import *

class User(Fact):
    """Info about the traffic light."""
    pass


class BaiQiShi(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.dic = {}

    @Rule(User(enterNetworkTimes=P(lambda x: x<= 796)))
    def hitEnterNetworkTimes(self):
        print('hitEnterNetworkTimes')
        self.dic['hit_enterNetworkTimes'] = 1

    @Rule(User(bqsThreeMonthMPL=P(lambda x: x >= 41)))
    def hitBqsThreeMonthMPL(self):
        self.dic['hit_bqsThreeMonthMPL'] = 1

    def result(self):
        return self.dic

engine = BaiQiShi()        
ua = User(enterNetworkTimes=794, bqsThreeMonthMPL=51)
engine.reset()
engine.declare(ua)
engine.run()   
print(engine.result())

