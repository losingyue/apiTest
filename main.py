from baseFuc.utilsFuc import ExcelUtil
from baseFuc.result_check import checkPoint
import requests
from baseFuc.url_requests import url_request
if __name__ == "__main__":
    filepath = "D:/apiTest/data.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    test=data.dict_data()
    reportdata=[]
    for i in range(len(test)):
        mothed =test[i]["mothed"]
        headers=test[i]["headers"]
        params=test[i]["params"]
        cookies=test[i]["cookies"]
        pre_checkPoint=test[i]["pre_checkPoint"]
        print(pre_checkPoint)
        if len(test[i]["headers"])>0:
            headers=eval(test[i]["headers"])
        if len(test[i]["params"])>0:
            params=eval(test[i]["params"])
        url=test[i]["URL"]
        if len(test[i]["cookies"])>0:
            cookies=eval(test[i]["cookies"])
        res=url_request(mothed,headers,params,url,cookies)
        results=res.request_get()
        print(results)
        diff_res=checkPoint(pre_checkPoint,results)
        diff_result=diff_res.diff()
        print(diff_result)