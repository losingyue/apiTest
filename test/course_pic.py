#coding:utf-8
import requests
import os
headers = {
    "Authorization": "bearer FpnxnWPej-lTsS_qx4dKVp_-j-MAiqqc9zIGhJzX1wNNx1FkQ66l6-Wvikh8ROELWWE1bXeyWWjHQG0qNcvNumzqkaAKa09Gw51OCG_aVIEJBjFpzkyq_eCoZnB4ETtjJzUi-V3LtuNC2F5zgH_mBeG0whjrRNKh_1kzMnxInvapBrqaVFbHU-JkMIFqnM-gpZw6CwS6YkU1VWmXy_ETxb_JLAc71WomTTQ01ocFeKF5S4SVHwTW_RXHrlwsFo70T99iNr61tfTyY5uqwKcU-Yiajwi7shGpyX-CCPHNf82q35pE",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN",
    "Content-Type":"application/json"
}
url2 = 'https://testtbprapi.yqj.cn/kwddj/home/book/catalog?book_id=42'
res = requests.get(url2, headers=headers,verify=False)
data = res.json()
data_list=data["data"]["book_tree"]
dic_pics=[]
dic_vids=[]
for i in range(len(data_list)):
    dic_pics.append(data_list[i]["page_url"])
print(dic_pics)

def download_pic(list_pic):
    for url in dic_pics:
        root = "D://testData//"
        path = root + (url.split("@")[0]).split("/")[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                r.raise_for_status()
                #使用with语句可以不用自己手动关闭已经打开的文件流
                with open(path,"wb") as f: #开始写文件，wb代表写二进制文件
                    f.write(r.content)
                print("爬取完成")
            else:
                print("文件已存在")
        except Exception as e:
            print("爬取失败:"+str(e))

def download_video(list_video):
    url1="http://yx-kbs-ks3.haofenshu.com/videos/f5113819e488ee4d6a2d478a0571e2b9.mp3"
    r = requests.get(url1, stream=True)
    with open('bigMall.mp3', "wb") as mp4:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)

    print("dowload over")
if __name__ == "__main__":
    download_video("test")