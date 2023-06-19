# Poe_QQ
[poe逆向工程](https://github.com/ading2210/poe-api)对接到QQ
# 准备工作
配置[mirai-api-http](https://github.com/project-mirai/mirai-api-http)，[配置示例](https://github.com/avilliai/wReply/blob/master/setting.yml)

了解你的代理(运行的端口号)
# 使用
## 获取你的token
- 打开代理进入poe.com(如果打不开说明你的代理不行，换。)
- 按下f12进入开发者模式，找到application(应用程序)，复制p-b项的值
- ![image](https://github.com/avilliai/Poe_QQ/assets/99066610/dd322993-237d-45e3-842c-17b50c127e2c)
## 填写config.json
- 用记事本打开config.json
```
{"botName": "yucca", "botQQ": "3093724179", "master": "1840094972","vertify_key":"1234567890","port":"23456","poeKEY":"your-Poe-KEY","proxy":"http://127.0.0.1:1080"}
```
- botName不用管，没写替换；botQQ填你在bot的qq；master填你的qq;
- vertify_key填你mirai-api-http配置的key;port填mirai-api-http配置的端口
- poeKEY填我们上面复制的p-b的值，proxy填你的代理地址(我的在本地的1080端口所以是http://127.0.0.1:1080)
## 运行
双击start.cmd

# 可用的指令
- /reload
- /reload指令用于重新加载，如果遇到卡死的情况，不过卡死的原因更可能是因为代理不行被poe鲨了，所以/reload并不能解决所有问题
- /clear
- /clear指令用于清空对话
# 其他
考试周了，做的比较匆忙，[poe逆向工程](https://github.com/ading2210/poe-api)的文档我还没看够一遍。
