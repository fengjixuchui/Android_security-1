# 非安全存储、加密、传输问题-AirDroid

## BG
AirDroid 是 remote management tool for Android。MITM攻击。信息泄露，rce  更新 apk 成 malisious 部分。

## Summary
AirDroid依赖于不安全的通信通道，便于将用于验证设备的相同数据发送到其统计服务器。此类请求使用DES加密，加密密钥在应用程序本身内部进行了硬编码。目标设备的同一网络上的任何恶意方可以进行MITM。

## 影响

grab device authentication information 。from HTTP request。
hardcoded key “890jklms” and from JSON 解析的 身份验证字段 在运行时解密此HTTP请求。

攻击者可以进行中间人攻击 向 AirDroid API端点执行各种HTTP或HTTPS请求。