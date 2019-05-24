# Content Injection in DuoLingo’s TinyCards App for Android
BG
以Android WebView为框架的Web应用程序。 

利用可能性有多大，
RCE、影响Android版本>=4.0，影响 < google play商店发布的v1.0版本

被利用之后产生什么样的效果
可以通过运行JavaScript导致JavaScript在应用程序中执行。根本原因是当初始Web内容加载到WebView时，应用程序启动时缺少SSL。