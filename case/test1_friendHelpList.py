#coding:utf-8
import unittest
import HTMLTestRunner
import time
import os,sys
import requests
class myTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_helpList(self):
        headers={
            "Authorization":"Bearer yJiDRiF7qvD2e_NgWcwn1JiW9qp_fZJae-YT1LipMZObFabAVCprktKbXs78imowlOHCnRHF9sHJxcco2X6M29NEKdJfQojKJvoSzCK_A2LA6MUSX5VTnCjPkH4Dc0yb6oJL4QE59bDA9ftW08Fm8UzINYlF0aasguCyUeN4xgXRQuxDhAw53hZ7IKAKwdek_018eUGZwy8flfYnlyDG86ELwI9mif3-FpdyPF0yZxgfDUat0PZJaQc--APVFLHSJh8gBL4Rybh0szkQb1I0DzXHtYudrALVcnMc-X9Iqg5b-lQ_VUkACQeEsYhmH5abhpPXcA"
        }
        url1='http://testwwwapi.yqj.cn/api/res/pal_assist/list?shop_id=108&status=1&skip=0&limit=10'
        res=requests.get(url1,headers=headers)
        data=res.json()
        self.assertIn("OK", data['Msg'])
        #assert "OK" in data
    def test_deleteList(self):
        headers = {
            "Authorization": "Bearer yJiDRiF7qvD2e_NgWcwn1JiW9qp_fZJae-YT1LipMZObFabAVCprktKbXs78imowlOHCnRHF9sHJxcco2X6M29NEKdJfQojKJvoSzCK_A2LA6MUSX5VTnCjPkH4Dc0yb6oJL4QE59bDA9ftW08Fm8UzINYlF0aasguCyUeN4xgXRQuxDhAw53hZ7IKAKwdek_018eUGZwy8flfYnlyDG86ELwI9mif3-FpdyPF0yZxgfDUat0PZJaQc--APVFLHSJh8gBL4Rybh0szkQb1I0DzXHtYudrALVcnMc-X9Iqg5b-lQ_VUkACQeEsYhmH5abhpPXcA"
        }
        url2='http://testwwwapi.yqj.cn/api/res/pal_assist/list?shop_id=108&status=0&skip=0&limit=10'
        res = requests.get(url2, headers=headers)
        data = res.json()
        self.assertIn("OK", data['Msg'])
    def tearDown(self):
        pass

if __name__=="__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(myTest("test_helpList"))
    testunit.addTest(myTest("test_deleteList"))
    HtmlFile = "D:/apiTest/result.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"接口测试报告", description=u"用例测试情况")
    runner.run(testunit)