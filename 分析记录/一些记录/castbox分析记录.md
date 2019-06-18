# CastBox

# castbox的功能

What and How

* Generic understanding on what the app does?
* Find ways to attack the app?

	Start from the "entry points"
	- Attack surface analysis

	Check the app's components (activities, etc.)
	- Can they be reachable from another app?

	Check how the app interacts with the external world
	- File-system, network, inter-component communications, etc.

* How does the app interact with network endpoints?
* How does it store private information? 还未
* Check whether a functionality can be abused?


## castbox功能

* 使用tensorflow 提供个性化推荐
* BoxWallet
* 解析音频
* 倒入、导出RSS xml功能

## 分析可以进行的下一步操作

### 1

    Castbox使用了Google开源的机器学习框架——TensorFlow以及自然语言处理（NLP）对用户偏好进行分析 ，从而提供精准的个性化推荐。
    为了确保算法的准确性，Castbox团队在TensorFlow的基础上加入了自己的影响因子

### 2

Castbox推出了一款新的加密货币钱包BoxWallet

--> wallet vulnerability

---> get 敏感信息
    捕wallet与货币的流量 case 
 	McAfee’s ‘unhackable’ cryptocurrency wallet has been hacked

---> 获取电话信息中授权的信息

	1.ss7 Signaling System No 7 (SS7) protocol  sms协议的漏洞
	    只要能获取到名字，姓氏和电话号码，研究人员就能够得到与钱包相关联的电子邮件地址，获得对钱包的控制权，并获得对钱包本身的访问权限，包括 撤回资金。
	    https://betanews.com/2017/09/18/network-flaws-bitcoin-wallets/
	    2017年

    2.webview 
	是一个 rce，解析html code ->auto dialer -> wallet
	2016年
	demo twitter、LinkedLn 

* 2018年6月1日，Castbox推出了一款新的加密货币钱包——BoxWallet，BoxWallet将被嵌入到Castbox中，用户可以直接在Castbox中进行以太坊和BOX代币的兑换。
为Castbox的区块链支付系统提供支持的正是此前与其达成战略合作关系的ContentBox

下一步-->xposed 捕捉流量
	除非能leak出密码，不然这么挖掘有什么意义呢

### 3

Castpod可以解析音频内容

下一步--> native层 使用的库

### 4

查看通信网络

check over

### 5

基于360显危镜
http://appscan.360.cn/app/d73e92b14f75e7706a0b8a9367cc7931/report/
* 下一步--> unzip解压缩
	Lcom/airbnb/lottie/f; b

	private static k b(ZipInputStream arg5, String arg6)

	判断是否可控可触发
	
	使用了 开源项目 lottie-android 
	lottie 使用同一个JSON动画文件，可实现酷炫动画效果
	https://github.com/airbnb/lottie-android
	最低支持API 16

	没有搜到aribnb/lottie 相关 漏洞消息

	看一看是否可达可控(我是不是哪里弄错了) 

	服务器下发指令 
	实现动画效果
	json 可能也带了一些资源
	达

	控

    抓取流量，发现该app，都是走的ssl流量。从网络上劫持 不可行。
    unzip解压缩，此处的来源都是从服务器下发指令。所以不可控




### 6

非安全存储
都用的是ssl加密协议

### 7

导出组件
fm.castbox.player.CastboxMediaReceiver 导出
继承于MediaButtonReceiver
接收多媒体按钮广播的，常用于耳机等多媒体设备的按键监听。
fm.castbox.player.CastboxMediaReceiver

接受指定包名的广播，translates，
是否可以伪造包， 不能算是安全问题
