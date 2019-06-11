# Messing with Android Apps

## 哪个组件 actually executing Dalvik?
Android4.4 之前
  - DVM，libdvm.so
  - 执行一个方法，编译并且run
  		编译程序， Dalvik 代码-> 机器码
  - 重解析，按需编译
  - 即时编译（JIT）
编译的代码存储在缓存里

## Android ART
ART stands for Android Run-Time
	It replaced the old DVM
	It was introduced in Android 4.4 as optional, mandatory in Android 5
Ahead-Of-Time compilation
	Compilation happens at app installation time

## New Version of ART 
It is pretty smart 
    