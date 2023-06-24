# Poe_QQ
poe-api对接到QQ

基于[poe-api](https://github.com/ading2210/poe-api)实现

**需要[安装mirai-api-http](https://github.com/project-mirai/mirai-api-http)并[配置](https://github.com/avilliai/wReply/blob/master/setting.yml)**

# 安装与配置
## 安装python(从release下载)
安装的时候记得第一步勾选add to path

安装完成后打开cmd执行如下指令
```
pip install yiri-mirai
pip install poe-api
```
## 抓取token
打开[poe官网](https://poe.com/)并完成注册(如果你打不开说明你的代理不行，换)

按下f12打开开发者模式，找到application(或应用程序)，然后打开cookies，复制里面p-b项的值，我们之后会用到。
![image](https://github.com/avilliai/Poe_QQ/assets/99066610/d7623cd9-09c3-41b8-bb0e-a9fa487b7fe7)

## 填写配置文件
打开config.json
```
{"botName": "yucca", "botQQ": "3093724179", "master": "1840094972","vertify_key":"1234567890","port":"23456","poeKEY":"your-Poe-KEY","proxy":"http://127.0.0.1:1080"}
```
- botName可以不用管，没写替换。botQQ填bot的qq，master填你的qq
- vertify_key填写你api-http中配置的key,port填写api-http中ws配置的端口(如果你使用[配置文件示例](https://github.com/avilliai/wReply/blob/master/setting.yml)可以忽略这部分)
- poeKEY填写上面我们抓取的p-b的内容，proxy填写你代理的端口，我的在本地的1080端口运行所以是http://127.0.0.1:1080
## 启动
运行bot.py即可

# 使用
/poe
- 如 /poe请介绍理塘艺术家丁真珍珠先生的主要作品
- 
/reload
- 用于掉线重连，仅master可用指令。如果/reload不起效看看账号是不是被封了或者代理是否依然有效

/clear
- 清空对话
# 其他
正在考试周，没有时间去实现api中的所有功能，等考完慢慢搓。
