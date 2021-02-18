from lib import hanshu
import requests
from requests_toolbelt import MultipartEncoder
import csv
import time
import os
import csv





# #遍历文件夹，将文件名写入文档
# for (root,dirs,files) in os.walk("D:/接口测试/jemter/save/PPG项目/ECG数据未标定/mimicecg1"):
#     for f in files:
#         old_path = os.path.join(root,f)
#         print(old_path)
#         with open('D:/接口测试/jemter/save/PPG项目/ECG数据未标定/112.csv','a',newline='')as f1:
#             spam = csv.writer(f1)
#             spam.writerow([old_path])
##遍历文件件，改文件名
# for (root,dirs,files) in os.walk("E:\old"):
#     i=1
#     j=1
#     for f in files:
#         old_path = os.path.join(root,f)
#         # 把文件名分解为 文件名.扩展名
#         # 在这里可以添加一个 filter，过滤掉不想复制的文件类型，或者文件名
#         (shotname, extension) = os.path.splitext(f)
#         # 原文件的路径
#         if 'old' in shotname:
#             new_name = "窦性"+str(i)+ extension
#             new_path = os.path.join("E:/new1", new_name)
#             # 新文件的路径
#             i = i + 1
#         elif 'new' in shotname:
#             new_name = "房颤"+str(j)+ extension
#             new_path = os.path.join("E:/new2", new_name)
#             # 新文件的路径
#             j = j + 1
#         open(new_path,'wb').write(open(old_path,'rb').read())




# for root,dirs,files in os.walk("D:\接口测试\jemter\save\PPG项目\PPG数据\房颤"):
#     print(root)
     # for dir in files:
     #     print(dir)
# with open('D:/接口测试/jemter/save/PPG项目/PPG数据/结论'+filetime1+'.csv', 'a', newline='') as f:
#  rows =file_idlist2
#  writer = csv.writer(f)
#写入多行数据
 # writer.writerows(rows)

 # for file in files:
 #  print os.path.join(root,file).decode('gbk').encode('utf-8');





# cishu=2
# list3=hanshu.gettxt("D:/接口测试/jemter/save/PPG项目/PPG数据/总2.txt",cishu)
# filetime1= time.strftime("%Y%m%d%H%M%S")
# j=0
# file_idlist2=[]
# while j<cishu:
#      file_idlist1 = []
#      filename1=list3[j][0]
#      fielpath=list3[j][1]
#      print(fielpath)
#      url='http://192.168.9.181:8081/pacs/ppg/upload'
#      data = MultipartEncoder(fields={'ppg': ('filename', open(fielpath, 'rb'), 'text/xml')})
#      restext0=requests.post(url=url,data=data,headers={ 'Content-Type': data.content_type,})
#      file_id=hanshu.strtodict(restext0.text)['file_id']
#      print(file_id)
#      file_idlist1.append(time.strftime("%Y-%m-%d %H:%M:%S"))
#      file_idlist1.append(file_id)
#      file_idlist1.append('窦性')
#      j=j+1
#      file_idlist2.append(file_idlist1)
#      print(file_idlist2)
#      with open('D:/接口测试/jemter/save/PPG项目/PPG数据/结论'+filetime1+'.csv', 'a', newline='') as f:
#         rows =file_idlist2
#         writer = csv.writer(f)
#     #写入多行数据
#         writer.writerows(rows)








# myfile=open("D:/接口测试/jemter/save/PPG项目/PPG数据/总2.txt")
# mylist=myfile.readlines()
# lines=len(mylist)
# list3=[]
# cishu=30
# cishu2=(cishu//lines)+1
# i=0
# while i<cishu2:
#     for line in open("D:/接口测试/jemter/save/PPG项目/PPG数据/总2.txt"):
#         list1=line.split(",")
#         list3.append(list1)
#     i=i+1
# list3=hanshu.gettxt("D:/接口测试/jemter/save/PPG项目/PPG数据/总2.txt",cishu)
# j=0
# while j<cishu:
#     print(list3[j][0])
#     print(list3[j][1])
#     j=j+1

