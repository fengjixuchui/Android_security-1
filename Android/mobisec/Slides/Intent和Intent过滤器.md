# Intent和Intent过滤器
https://developer.android.com/guide/components/intents-filters

> start Activity
	Activity 表示应用中的一个屏幕。通过将 Intent 传递给 startActivity()，您可以启动新的 Activity 实例。Intent 描述了要启动的 Activity，并携带了任何必要的数据。
	如果您希望在 Activity 完成后收到结果，请调用 startActivityForResult()。在 Activity 的 onActivityResult() 回调中，您的 Activity 将结果作为单独的 Intent 对象接收。

> start Service
	Service 是一个不使用用户界面而在后台执行操作的组件。通过将 Intent 传递给 startService()，您可以启动服务执行一次性操作（例如，下载文件）。Intent 描述了要启动的服务，并携带了任何必要的数据。
    如果服务旨在使用客户端-服务器接口，则通过将 Intent 传递给 bindService()，您可以从其他组件绑定到此服务。

> 传递广播

## 构建Intent

Intent对象携带Android系统用来确认要启动哪个组件的信息，以及收件人组件为了正确执行操作而使用的信息。
主要包括：
* 组件名称
	有->显式，无->隐式。<ComponentName>对象com.example.ExampleActivity。您可以使用setComponent()、setClass()、setClassName() 或 Intent 构造函数设置组件名称。
* 操作
	指定要执行的通用操作的字符串。
* 数据
	URI,由ContentProvider控制，仅设置数据URI，调用setData()。仅设置MIME类型，调用setType()
* 类别
Intent 可能会携带不影响其如何解析为应用组件的信息。
* Extra
* 标志