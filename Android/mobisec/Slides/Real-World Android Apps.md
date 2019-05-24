# Real-World Android Apps
"complicated" things about real-world apps
很多things 被恶意软件使用 or security repercussions。

* 签名
- 每个app 都 signed with a certificate
- certificate is
	公钥、其他metadata identifying
- 认证的owner拥有回应的私钥

* 加密签名入门
- 生成密钥对 -> 拥有者保持priv -> pub public。
- 两个最重要的 -> sign & verify
- sign(MESSAGE,PRIVE) ->SIGN
- verify(MESSAGE,SIGN,PUB) -> VALID/NOT VALID

- 认证不需要证书签名 or 权威
	app的认证可以 自我认证
	与SSL认证主要的区别在于：SSL证书可以自签名，但是默认不受信任。
- 区分 app的作者，不能定义他们
- 区分“system" vs ”normal“apps
	"system" app “system”签名
	这就是系统如何处理“signature”权限
- 比如 我可以确定 给 Facebook app签名的和另一个Messenger app一样。但是无法确定Facebook app是官方的那一个。

* app认证与SSL认证
- SSL认证是 该网站最终由我浏览器所信任的网站所签名

* android:sharedUserId
	将与其他应用程序共享的Linux用户标识的名称。默认情况下，Android会为每个应用分配自己唯一的用户ID。但是，如果此属性设置为两个或多个应用程序的相同值，则它们将共享相同的ID  - 前提是它们的证书集相同。具有相同用户ID的应用程序可以访问彼此的数据，并且如果需要，可以在同一进程中运行。

* Resources
	static content that app uses
	drawable,layout,raw，
	values(arrays,colors,strings)

* RunTime.exec()
	 C's system() or Python's os.system()
	 Runtime.exec("cp ../flag /sdcard/leaked-flag.txt")

* Java反射
获取Class对象的三种方法
	静态.class方法获取，任何数据类型都有静态class方法直接获取Class对象，但是没有这个类就无法调用。
	通过getClass()方法，该对象的getClass()方法可以获取该类的Class文件，需要导入对象。
	通过Class.forName(String name)通过一个类的全限定名，拿到其Class对象，不需要任何支持。

* 动态代码加载
	apps 可以 "load" 额外的代码在 run-time
	代码可以来自 file-system
		mean it's can be embedded in the app itself
		"just-downloaded" piece of code
	benign apps do this to
		- a/b testing
		- sharing common framework
		- download additional parts

* 序列化
	- 序列化版本
		编码细节 Peppa特定实例的详细信息
		does NOT 编码 Peppa的实际定义
	- 从原始字节加载Peppa 
		您的代码需要在可见类中包含Peppa的定义

	- 在通过Binder发送之前，对象需要序列化

	- Example:Intents!

	- Two main interfaces
		- Parcelable
			- instance 可以从 Parcel 中 written to/ restored from
			- Parcel，通过Binder 发送的对象的容器
		- Serializable
			- 可序列化接口