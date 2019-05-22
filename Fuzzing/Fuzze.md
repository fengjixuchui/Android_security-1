# Fuzzer
* 何时结束Fuzzing工作
* afl-fuzz生成了哪些文件
* 如何对产生的crash进行验证和分类
* 用什么来评估Fuzzing的结果
* 代码覆盖率及相关概念
* AFL是如何记录代码覆盖率的

* AFL介绍 
#TODO
ref：https://blog.csdn.net/abcdyzhang/article/details/53727221

## 其他工具

### afl-cmin
	需要一个给定的包含可能的test case文件夹，然后运行每一个并将收到的反馈与所有其他test case进行比对，找到最有效表示 最 unique的代码路径的最好的test case。并保存到一个新的目录。
### afl-tmin
	用于指定的文件，为了使每一个test case达到表示与原始测试用例相同的代码路径所需的最小值，afl-tmin遍历test case的实际字节，逐步删除很小的数据块，直到删除任意字节都会影响到代码路径表示。