FROM python:3.7.12

MAINTAINER yixin.hu <yixin.hu@139.com>

#ENV App_url=www.baidu.com
#ENV App_robotUrl=none
#ENV App_alarmSwitch=off
#ENV App_alarmLevel=99999999999999

#输出python文件显示（好像没用）
ENV PYTHONUNBUFFERED=0

WORKDIR /opt/
COPY requirements.txt /tmp

ADD ./* /opt

RUN set -ex \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian stretch main contrib non-free" >>/etc/apt/sources.list \
    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian stretch-updates main contrib non-free" >>/etc/apt/sources.list \
    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free" >>/etc/apt/sources.list \
#    && apt-get update \
#    && apt-get install -y git \
#    && git config --global user.email "auto@whrd.work" \
#    && git config --global user.name "auto自动化" \
    && python -m pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple --upgrade pip \
    && pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple -r /tmp/requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

#CMD ["python","/opt/monitor_cert.py"]
CMD ["python","/opt/run.py"]
#CMD ["top","-b"] 
#



# 构建镜像：docker build -t harbor.wh.ctrm/library/python:3.10.0-autotest-web-1015 .
# 可跳过，镜像打Tag：docker tag python:3.10.0-autotest-web-1015 harbor.wh.ctrm/library/python:3.10.0-autotest-web-1015
# 推送镜像：docker push harbor.wh.ctrm/library/python:3.10.0-autotest-web-1015
# windows本地Docker调试：docker run -it --name autotest --rm -v /mnt/d/pm-gitlab-dcp2/dcp-api-autotest:/opt harbor.wh.ctrm/library/python:3.10.0-autotest-web-1015 python run_All_case.py
# 交互式方式生成一个容器调试：docker run -it --name python --rm harbor.wh.ctrm/library/python:3.10.0-autotest-web-1015 bash



