# coding:utf-8
import requests
import json
class url_request():
    def __init__(self,mothed,headers,params,url,cookies):
        self.params=params
        self.headers=headers
        self.mothed=mothed
        self.url=url
        self.cookies=cookies

    def request_get(self):
        #params=jself.params
        headers=self.headers
        mothed=self.mothed
        url=self.url
        cookies=self.cookies
        print(headers,mothed,url,cookies)
        res=requests.get(url,headers=headers,cookies=cookies)
        return res.json()

    def request_post(self):
        params=self.params
        headers=self.headers
        mothed=self.mothed
        url=self.url
        if mothed=="get":
            res=requests.get(url,headers=headers)