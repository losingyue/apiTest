from threading import Timer
from wxpy import *
import requests

class Wechat:
    receiver = ''  # 为接受者的微信昵称
    second_receiver = ''  # 第二接受者的昵称
    def __init__(self, receiver, second_receiver):
        self.receiver = receiver
        self.second_receiver = second_receiver

    def get_news(self):
        url = "http://open.iciba.com/dsapi/"  # 调用金山词霸每日一句开放接口
        r = requests.get(url)  # 获取网页数据，数据格式为json
        content = r.json()['content']
        note = r.json()['note']
        fenxiang_img = r.json()['fenxiang_img']
        return content, note, fenxiang_img

    def send_news(self):
        bot = Bot()  # 实例化机器人对象
        try:
            contents = self.get_news()  # 获取发送消息内容
            my_friend = bot.friends().search(self.receiver)[0]  # 将第一个昵称为receiver的微信好友作为消息接受者
            my_friend.send(contents[0])  # 发送每日一句的content
            my_friend.send(contents[1])  # 发送note
            my_friend.send(contents[2])  # 发送图片
            # 每86400秒（1天），发送1次
            t = Timer(86400, self.send_news)
            t.start()
        except:
            my_friend = bot.friends().search(self.second_receiver)[0]  # 如果第一个接受者发送失败，则发送给第二个
            my_friend.send(u"今天消息发送失败了")  # 发送提示错误消息

if __name__ == '__main__':
    wechat = Wechat('Test', 'Test_________2')
    wechat.send_news()