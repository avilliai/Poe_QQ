# -*- coding:utf-8 -*-
import datetime
import json

import poe
from mirai import Image, Voice, Startup
from mirai import Mirai, WebSocketAdapter, GroupMessage
from mirai.models import BotInvitedJoinGroupRequestEvent,NewFriendRequestEvent



if __name__ == '__main__':
    with open('config.json','r',encoding='utf-8') as fp:
        data=fp.read()
    config=json.loads(data)
    qq=int(config.get('botQQ'))
    key=config.get("vertify_key")
    port= int(config.get("port"))
    bot = Mirai(qq, adapter=WebSocketAdapter(
        verify_key=key, host='localhost', port=port
    ))


    botName = config.get('botName')
    master=int(config.get('master'))
    #填写你的poe-token
    poeKEY=config.get('poeKEY')
    proxy = config.get('proxy')


    def startVer():
        file_object = open("./mylog.log")
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        print(all_the_text)

    try:
        global client
        client = poe.Client(poeKEY, proxy=proxy)
        json.dumps(client.bot_names, indent=2)
        mes="早上好"
        str2=""
        for chunk in client.send_message("capybara", mes):
            # print(chunk["text_new"],end="", flush=True)
            str += chunk["text_new"]
        print("bot:" + str2)
    except:
        print("出错，请检查代理配置或更新token。")


    @bot.on(GroupMessage)
    async def AiHelper(event: GroupMessage):
        global client
        if str(event.message_chain).startswith("/poe"):
            mes = str(event.message_chain)[4:]
            s = ""
            try:
                for chunk in client.send_message("capybara", mes):
                    # print(chunk["text_new"],end="", flush=True)
                    s += chunk["text_new"]
                print("bot:" + s)
                await bot.send(event, s)
            except:
                await bot.send(event, "出错，达到每分钟限制或token已失效。")
        if str(event.message_chain) == "/clear" and str(event.sender.id) == str(master):
            client.send_chat_break("capybara")
            await bot.send(event, "已清除对话上下文。")
        if str(event.message_chain) == "/reload" and str(event.sender.id) == str(master):
            client = poe.Client(poeKEY, proxy=proxy)
            json.dumps(client.bot_names, indent=2)
            await bot.send(event, "已重启")
    startVer()
    bot.run()