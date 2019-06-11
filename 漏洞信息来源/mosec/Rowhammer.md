# Rowhammer
“风水翻转”攻击技术
计算机Memory介质中，每个存储单元存放1bit数据，存储单元中充满电子表示1，清空表示0.
存储数据的内存由上亿这样的存储单元构成。但电容器会泄露，一个电容器充满电子后，只需要几毫秒就会泄露殆尽。需要CPU对电容器进行充电。充电就是由CPU先读取电容器中的值，然后再把数据写回去。这种刷新操作，每秒会执行几千次。
然而，这几年内存容量大幅度上涨，所以存储比特位的电容器也就越来越小，排列越来越近。要防止相邻的电容之间相互干扰，难度也就变得更大。如果能够快速、反复访问一排电容，相邻行的电容更容易产生干扰错误和所谓的“比特位翻转”，也就是0变成1。
这种情况如果对某些行进行反复读写，问题就有可能产生。
利用比特位翻转，很多事情都可以做，比如说执行未经授权的代码。这就是所谓的Rowhammer。

## 关于安卓的RowHamer
ref: https://www.anquanke.com/post/id/150881
成功利用Rowhammer，攻击者必须诱使系统加载目标内存到DRAM中与攻击者所有的物理内存行邻接的行中。

目前已有的Rowhammer攻击有GLitch、Throwhammer、Nethammer等。

1. Glitch：该技术使用嵌入的GPU来实施针对安卓设备的Rowhammer攻击。
2. Throwhammer：利用已知的DRAM漏洞利用使用远程直接内存访问（remote direct memory access，RDMA）信道通过网卡发起攻击，这是第一个基于网络的远程Rowhammer攻击方式。
3. Nethammer：也是一个基于网络的远程Rowhammer攻击方法。在处理网络请求时通过未缓存的内存或flush指令来攻击系统。

## Google对基于Rowhammer攻击的缓解措施
2016年，google 关闭了负责连接内存分配的icon组件（kmalloc heap）。
