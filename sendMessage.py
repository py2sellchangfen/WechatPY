from wechatpy import WeChatClient

def sendmessage(userid, content):
    client = WeChatClient('wx62f41dbfd6a4b6ba', '732d1e0da0e921ab33a95ba3adaad356')
    client.message.send_text(userid, content)








