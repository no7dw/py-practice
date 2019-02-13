# verify python redis pub sub lantency

background: 在做高频交易系统 HFT，用了redis 做pub sub 通知，发现这种方法竟然消耗了6~7ms。低延时是这个系统的关键，相对于一个ping round：

`
    ubuntu@VM-0-7-ubuntu:~$ ping www.okex.com
    PING wwwapistarx.okex.com (47.75.99.233) 56(84) bytes of data.
    64 bytes from 47.75.99.233: icmp_seq=1 ttl=92 time=1.13 ms
    64 bytes from 47.75.99.233: icmp_seq=2 ttl=92 time=1.14 ms
`

这个redis 的pub sub 延时,相对于ping okex round trip 作为一个beanchmark ，是巨大的。

行业需要：
"
一般的做法:
不考虑策略开销，不考虑策略全跑在FPGA的情况，最好把tick to order压缩到5微秒以下。
"

[from here](https://www.zhihu.com/question/28630922)

于是去研究了下一些原因：

##进一步看为什么这么“高”的延时
  
  - 版本说明 redis 5.0, python 3.7 ,机器本身 2015 macbook pro , macOS Mojave 10.14.2 


 
    dengwei@RMBAP:~/projects/github/no7dw/py-practice/latency$  redis-cli --intrinsic-latency 100
    Max latency so far: 1 microseconds.
    Max latency so far: 15 microseconds.
    Max latency so far: 16 microseconds.
    Max latency so far: 69 microseconds.
    Max latency so far: 87 microseconds.
    Max latency so far: 89 microseconds.
    Max latency so far: 241 microseconds.
     Max latency so far: 246 microseconds.
    Max latency so far: 293 microseconds.
    Max latency so far: 304 microseconds.
    Max latency so far: 609 microseconds.
    Max latency so far: 759 microseconds.
    Max latency so far: 976 microseconds.
    Max latency so far: 1101 microseconds.
    Max latency so far: 1282 microseconds.
    Max latency so far: 13483 microseconds.
    
    1622524817 total runs (avg latency: 0.0616 microseconds / 61.63 nanoseconds per run).
    Worst run took 218765x longer than the average latency.
   
    这个数据含义：机器的perf最糟糕的0.013 ms （millseconds），与redis 无关，是机器本身的问题

  - [优化](https://redis.io/topics/latency)：
    - 使用本地的redis（已经是）
    - disable AOF 
      
```
   redis-server --save "" --appendonly no
```


  其他貌似不是要紧，这样不输出RDB文件后，publish 提升了 0.001621 s -- 1.6ms , subscript 0.002651 s -- 2.6ms ,perf: publish： 6.4ms, subscript :5.1ms

运行的命令：

```
for i in {1..19};do python3 p.py p ; done
```


但[这里](https://bravenewgeek.com/benchmarking-message-queue-latency/)显示一些mq的延时(for 1KB data, 99.99% percentile 点数据):
RabbitMQ  12ms 
kafka 13 ms v0.9
redis 1.5ms
nat 1.2ms

这个数据与实际测试有出入，可能是受限于python本身


more:

https://stackoverflow.com/questions/36183606/whats-google-cloud-pub-sub-latency

https://redis.io/topics/persistence

https://stackoverflow.com/questions/10557826/node-js-socket-io-redis-pub-sub-high-volume-low-latency-difficulties/11023625#11023625