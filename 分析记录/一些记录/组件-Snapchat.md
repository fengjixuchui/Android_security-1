# 组件-Snapchat

Description:
Java script injected in activity: 
net.hockeyapp.android.UpdateActivity with injection String: document.getElementsByTagName('body')[0].setAttribute('style', 'background-color: red');

net.hockeyapp.android.UpdateActivity

document.getElementsByTagName('body')[0].setAttribute('style', 'background-color: red');

result in information theft.

## 漏洞类型
逻辑漏洞

## 可利用性：
requires hockeyapp（a third party）to have an XSS vulnerability。

## 解决措施：
1.确保 JavaScript 、Plugin 是 Disabled for any WebViews。
2.All UIWebView call 不能执行，当没有合适的input的时候。 过滤危险的JavaScript 自负。使用白名单黑名单。
