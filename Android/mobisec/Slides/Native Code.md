# Native Code
Native Code 混淆
写与逆 apps

组件可以更快
Android让开发者写 CPU密集型组件

C/C++ -> /.so 

可靠的Dalvik拆解是“easy”
	主要得益于Dalvik字节码验证器
	字节码需要遵循一些属性......
	...这使它易于拆卸/分析

Java / Dalvik代码和本机代码都在同一安全沙箱中运行
	本机代码可能会干扰Dalvik代码/内存

	本机代码可以修改内存数据结构......
	Java代码调用方法A ...
	...而是调用方法B.

一般地说：Java /本机代码之间没有障碍

如果应用程序使用本机代码而您不知道它的作用，那么您无法完全信任您对Java世界的看法！
一切都以同一个用户身份运行

Java <- -> C/C++ with 
.class		.so		JNI(Java Native Interface)

At compilation time
	- APK content
	  - classes.dex
	  - ...
	  - lib/armeabi-v7a/native-lib.so
	  - lib/x86/native-lib.so
At installation time
	- The system takes all .so files it finds in libs/armeabi-v7a and it unpacks them  into /data/data/<your.package>/lib directory


