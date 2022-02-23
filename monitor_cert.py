#!/usr/bin/python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# @Time : 2021/08/31 18:40
# @Author : huyixin
# @File : monitor_cert.py
# @Version : 1.0
# --------------------------------------------------
#检查当前状态
# python monitor_cert.py
#每30分钟检查，低于告警阈值发送飞书告警（crontab配置）
#*/30 * * * * python /home/appop/elasticsearch_wildcard/monitor_cert.py
# --------------------------------------------------
#域名列表
#url = ["dev.open.10086.cn","dev.coc.10086.cn","xk.coc.10086.cn"]
# ------------------------飞书告警--------------------------
#机器人地址
#robotUrl = "https://open.feishu.cn/open-apis/bot/v2/hook/96c43be3-a882-4d1b-b6f3-25cda77f1b76"
#飞书告警开关(on/off)
#alarmSwitch = "on"
#告警阈值(过期天数告警)
#alarmLevel = '123'
# --------------------------------------------------
import os
import sys
import time
import json
import requests
import schedule
from urllib3.contrib import pyopenssl as reqs
from datetime import datetime

#容器日志输出
import logging
logging.basicConfig(stream=sys.stdout,level=logging.NOTSET,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

sys.path.append('./conf/')   
from config import * 

#自适应断python版本解决python2环境字符问题--beta
import sys
print(" * Python Version Is " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro))
if not sys.version_info.major >= 3 and sys.version_info.minor >= 0:
    print(" * Python <= 3")
    reload(sys)
    sys.setdefaultencoding('utf-8')
else:
    print(" * Python >= 3")

#如果存在环境变量则取环境变量
if os.getenv('robotUrl') is not None:
    robotUrl=(os.getenv('robotUrl'))
if os.getenv('alarmSwitch') is not None:
    alarmSwitch=(os.getenv('alarmSwitch'))
if os.getenv('alarmLevel') is not None:
    alarmLevel=(os.getenv('alarmLevel'))

#取证书并判断是否告警
def get_expire_time(url):
    cert = reqs.OpenSSL.crypto.load_certificate(reqs.OpenSSL.crypto.FILETYPE_PEM,reqs.ssl.get_server_certificate((url, 443)))
    notafter = datetime.strptime(cert.get_notAfter().decode()[0:-1], '%Y%m%d%H%M%S')  # 获取到的时间戳格式是ans.1的，需要转换
    remain_days = notafter - datetime.now()  # 用证书到期时间减去当前时间

    #print("查询域名" + str(url))   #获取当前查询域名
    #print("证书到期时间" + str(notafter))   #获取证书到期时间
    #print("证书剩余天数" + str(remain_days.days))  #获取剩余天数

    #Json输出
    jsonData={}
    jsonData["url"]=str(url)
    jsonData["expire"]=str(notafter)
    jsonData["remain"]=int(remain_days.days)
    print(json.dumps(jsonData))
    
    #判断告警并发送
    if int(remain_days.days) <= int(alarmLevel):
        print("{\"剩余天数不足告警\":"+ str(remain_days.days) + ",\"阈值\":" + alarmLevel + "}\n")
        logging.debug("{\"剩余天数不足告警\":"+ str(remain_days.days) + ",\"阈值\":" + alarmLevel + "}\n")
        if alarmSwitch == "on":
            py=("域名证书日期告警：(阈值:" + alarmLevel + ")""\n" + json.dumps(jsonData))
            alarm_feishu(py)

    #return py

#调用飞书接口
def alarm_feishu(py):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    global url
    url = robotUrl
    pyload = {
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": "开发平台证书续期通知""\n",
                "content": [
                    [
                        {
                            "tag": "text",
                            "text": py
                        }
                    ]
                ]
            }
        }
    }
}   
#    pyload = {
#    "msg_type": "text",
#    "content": {
#        "text": py
#    }
#}
    response = requests.post(url,data=json.dumps(pyload), headers=headers).text
    #print(response)


if __name__ == '__main__':
    
    #with open('domains.txt', 'r') as urls:
    for urls in url:
        get_expire_time(urls)

'''
try:
	while True:
		time.sleep(1000000)


#程序中止时清理GPIO资源
except KeyboardInterrupt:
	print('program stopped !')
'''