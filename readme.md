## 公网域名证书告警
该程序会校验证书时间，可配置简单定时任务，并发送飞书通知，需要公网能正常访问对应域名

### 配置文件
修改config.py

### 使用k8s configmap
配置文件挂载路径/opt/config.py 子路径: config.py

### 添加私有域名
通过编辑hosts文件可添加私有域名
配置文件挂载路径/etc/hosts 子路径: hosts