import subprocess
from monitor_cert import * 
#sys.path.append('./conf/')   
from config import * 


def run():
    #subprocess.check_output(["python", "./monitor_cert.py"])
    logging.debug(subprocess.check_output(["python", "./monitor_cert.py"]))

#判断配置
if schMinutesEnable == "on":
    schedule.every(int(schMinutes)).minutes.do(run)
elif schHourEnable == "on":
    schedule.every(int(schHour)).hour.do(run)
elif schDateEnable == "on":
    schedule.every().day.at(schDate).do(run)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

#程序中止时清理GPIO资源
except KeyboardInterrupt:
	print('program stopped !')