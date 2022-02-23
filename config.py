# ------------------------域名列表--------------------------
#需要查询的域名
url = ["dev.open.10086.cn","dev.coc.10086.cn","xk.coc.10086.cn","hd.coc.10086.cn","sandbox.open.10086.cn"]
# ------------------------飞书告警--------------------------
#飞书机器人地址
#测试告警群
robotUrl = "https://open.feishu.cn/open-apis/bot/v2/hook/96c43be3-a882-4d1b-b6f3-25cda77f1b76"
#生产告警群
#robotUrl = "https://open.feishu.cn/open-apis/bot/v2/hook/f39e0ab1-0bf8-483d-a487-d6e3327d1954"
#飞书告警开关(on/off)
alarmSwitch = "on"
#告警阈值(域名剩余天数)
alarmLevel = '30'
# ------------------------定时任务--------------------------
#简单的定时任务,建议选一个打开
#每隔几分钟执行
schMinutes = "1"
schMinutesEnable = "on"
#每隔几小时执行
schHour = "1"
schHourEnable = "off"
#每隔天几点执行
schDate="09:00"
schDateEnable = "off"



