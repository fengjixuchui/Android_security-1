# Android framework versions/API levels

API 级别是一个对 Android 平台版本提供的框架 API 修订版进行唯一标识的整数值。
Android 平台提供了一种框架 API，应用可利用它与底层 Android 系统进行交互。 该框架 API 由以下部分组成：
	一组核心软件包和类
	一组用于声明清单文件的 XML 元素和属性
	一组用于声明和访问资源的 XML 元素和属性
	一组 Intent
	一组应用可请求的权限，以及系统中包括的权限强制执行。
每个后续版本的Android平台 均可包括对其提供的 Android 应用框架 API 的更新。

API级别在Android中的使用
API级别标识符在确保尽可能为用户和应用开发者提供最佳体验方面发挥重要作用
每个 Android 平台版本都将其 API 级别标识符存储在 Android 系统自身内部。
应用可以利用框架 API 提供的清单元素 (<uses-sdk>) 来说明其可以运行的最低和最高 API 级别，以及其在设计上支持的首选 API 级别。 该元素具有以下三个重要属性：

	android:minSdkVersion - 指定能够运行应用的最低 API 级别。 默认值为“1”。
	android:targetSdkVersion - 指定运行应用的目标 API 级别。 在某些情况下，这允许应用使用在目标 API 级别中定义的清单文件元素或行为，而不是仅限于使用那些针对最低 API 级别定义的元素。
	android:maxSdkVersion - 指定能够运行应用的最高 API 级别。 重要说明：在使用该属性之前，请先阅读 <uses-sdk> 文档。

应用在 android:minSdkVersion 中声明 API 级别的主要原因是，告知 Android 系统，它使用了在指定 API 级别引入的 API。 如果由于某种原因将应用安装在 API 级别更低的平台上，则它会在运行时试图访问不存在的 API 时发生崩溃。系统通过在应用需要的最低 API 级别高于目标设备上的平台版本时不允许安装应用来防止出现这种结果。

