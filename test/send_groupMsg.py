from threading import Timer
from wxpy import *
import requests
import xlrd
from time import sleep
class Wechat:
    receiver = ''  # 为接受者的微信昵称
    second_receiver = ''  # 第二接受者的昵称
    def __init__(self, receiver, second_receiver):
        self.receiver = receiver
        self.second_receiver = second_receiver
    def get_msg(self):
        list_msg=[]
        pathfile='D:/标准动作.xlsx'
        #pathfile = 'D:/敏感词库表统计.xlsx'
        data = xlrd.open_workbook(pathfile)

        table = data.sheet_by_name('Sheet1')
        rowNum = table.nrows
        for i in range(1,rowNum):
            msg=table.cell(i,1).value
            list_msg.append(msg)
        return list_msg
    def send_news(self):
        bot = Bot()  # 实例化机器人对象
        my_friends_list = bot.friends()
        print(len(my_friends_list))  # 微信好友总数
        my_groups_list = bot.groups()
        print(my_groups_list)
        try:
            list_msg = self.get_msg() # 获取发送消息内容
            my_friend = bot.groups().search(self.receiver)[0]  # 将第一个昵称为receiver的微信好友作为消息接受者
            for i in range(30):#len(list_msg)
                my_friend.send(list_msg[i])  # 发送每日一句的content
                sleep(1)
        except:
            my_friend = bot.groups().search(self.second_receiver)[0]  # 如果第一个接受者发送失败，则发送给第二个
            my_friend.send(u"今天消息发送失败了")  # 发送提示错误消息

if __name__ == '__main__':
    wechat = Wechat('测试一号','测试一')
    wechat.send_news()
