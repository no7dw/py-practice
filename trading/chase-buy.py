# !/usr/local/bin/python
# -*- coding: UTF-8 -*-
'''backtest
start: 2018-02-19 00:00:00
end: 2018-02-20 12:00:00
period: 5m
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD","balance":10000,"stocks":3}]
'''
import sys
#sys.path.append("/usr/local/lib/python2.7/site-packages")    # 测试时添加了路径，如不需要可以删除
import time
from fmz import *
import math
import talib

task = VCtx(__doc__) # initialize backtest engine from __doc__

# ------------------------------ 策略部分开始 --------------------------
#pre = {}
print(exchange.GetAccount())     # 调用一些接口，打印其返回值。
pre = exchange.GetTicker()

def adjustFloat(v):             # 策略中自定义的函数
    v = math.floor(v * 1000)
    return v / 1000

# 最简单版追涨(杀跌)
def onTick(e):
    #Log("onTick")
    #print('on tick e',e.GetAccount())
    global pre
    amount = 0.1
    ac = e.GetAccount() 
    now = e.GetTicker()
    print(now['Last'], pre['Last'], ac['Balance'])
    if(now['Last'] > pre['Last'] and ac['Balance']>amount):
        print('buy', amount)
        e.Buy(-1, amount)
    pre = e.GetTicker()
    # ....

#
# ...
# 
# 此处省略 自定义函数实现等代码。

def main():
    InitAccount = exchange.GetAccount()
    
    while True:
        onTick(exchange)
        #time.sleep(1)
# ------------------------------ 策略部分结束 --------------------------

try:
    main()
except Exception as e:
    print(e)
    print(task.Join())          # print(backtest result  , 打印回测结果。
