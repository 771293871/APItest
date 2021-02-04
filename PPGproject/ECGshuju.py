import requests
from lib import hanshu
import time
import xlrd
import openpyxl
import pytest
import json
import ast
import time
from requests_toolbelt import MultipartEncoder
import csv



cishu=2
list3=hanshu.gettxt("D:/接口测试/jemter/save/PPG项目/PPG数据/总2.txt",cishu)
filetime1= time.strftime("%Y%m%d%H%M%S")
result=[]
j=0
while j<cishu:
     fileresult=[]
     filename1=list3[j][0]
     fielpath=list3[j][1]
     print(fielpath)

     url='http://192.168.9.181:8081/pacs/ppg/upload'
     data = MultipartEncoder(fields={'ppg': ('filename', open(fielpath, 'rb'), 'text/xml')})
     restext0=requests.post(url=url,data=data,headers={ 'Content-Type': data.content_type,})
     file_id=hanshu.strtodict(restext0.text)['file_id']
     print(file_id)

     url='http://192.168.9.181:8081/pacs/ppg/data_filter'
     data={"freq":125,"file_id":file_id}
     restext1=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print('1:')
     url='http://192.168.9.136:8188/get'
     data={"freq":200,"file_id":file_id}
     restext2=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print('2-1:')
     print(type(restext2.text))
     dst1=(hanshu.strtodict(restext2.text))['dst']
     print('2-2:')
     length1=(hanshu.strtodict(restext2.text))['length']

     # time.sleep(40)
     url='http://192.168.9.181:8081/pacs/ppg/rr_analysis'
     data={"freq":200,"data":dst1,"length":length1}
     restext=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print('3:')

     url='http://192.168.9.136:8188/get'
     data={}
     restext3=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print('4:')
     filerrArray1=(hanshu.strtodict(restext3.text))['rrArray']
     filelen_rr1=(hanshu.strtodict(restext3.text))['len_rr']

     url='http://192.168.9.181:8081/pacs/ppg/model_analysis'
     data={"file_id":file_id,"rrArray":filerrArray1,"len_rr":filelen_rr1,"size":1000 }
     restext=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print('5:')

     url='http://192.168.9.136:8188/get'
     data={"file_id":file_id,"feature_scatter":[0,0,0], "len_feature_scatter":0 ,"len_rr":filelen_rr1, "size":1000}
     restext=requests.post(url=url,json=data,headers={'Content-Type':'application/json'})
     print(restext.text)
     img_path1=(hanshu.strtodict(restext.text))['img_path']
     print(img_path1)
     dst1=(hanshu.strtodict(restext.text))['dst']

     url='http://192.168.9.181:8081/pacs/download_file?file_path='+img_path1
     r = requests.get(url)
     filename='D:/接口测试/jemter/save/PPG项目/PPG数据/窦性'+time.strftime("%Y%m%d%H%M%S")+".png"
     with open(filename, "wb") as code:
          code.write(r.content)
     fileresult.append(time.strftime("%Y-%m-%d %H:%M:%S"))
     fileresult.append(file_id)
     fileresult.append(dst1)
     fileresult.append(img_path1)
     j=j+1
     result.append(fileresult)
     with open('D:/接口测试/jemter/save/PPG项目/PPG数据/结论' +filetime1+ '.csv', 'a', newline='') as f:
          rows = result
          writer = csv.writer(f)
          # 写入多行数据
          writer.writerows(rows)


