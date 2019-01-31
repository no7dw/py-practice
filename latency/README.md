# verify python redis pub sub lantency

# publish before and after

before publish 1548901116.798094
after publish 1548901116.807091

latency

diff 0.008996963500976562

# subscript latency

diff 0.009057998657226562
diff 0.008563995361328125
diff 0.007433176040649414
diff 0.007539987564086914
diff 0.0056400299072265625
diff 0.006515979766845703
diff 0.03598618507385254
diff 0.01363992691040039
diff 0.0060918331146240234
diff 0.0049381256103515625

#conclusion

`
    ubuntu@VM-0-7-ubuntu:~$ ping www.okex.com
    PING wwwapistarx.okex.com (47.75.99.233) 56(84) bytes of data.
    64 bytes from 47.75.99.233: icmp_seq=1 ttl=92 time=1.13 ms
    64 bytes from 47.75.99.233: icmp_seq=2 ttl=92 time=1.14 ms
`

这个redis 的pub sub 延时,相对于ping okex round trip 作为一个beanchmark ，是巨大的。

"
一般的做法:

不考虑策略开销，不考虑策略全跑在FPGA的情况，最好把tick to order压缩到5微秒以下。
"

from: https://www.zhihu.com/question/28630922

