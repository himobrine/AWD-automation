```
平台密码可能默认toor

SSH密码修改：
passwd


mysql密码修改
show databases;
use mysql;
set password for root@localhost = password('123');

修改root用户的密码



#刷新配置
flush privileges;


mysq服务启动：
systemctl start mysql
systemctl status mysql


后台弱口令修改

kali里面开启apache2服务
service apache2 start


linux查看开放端口命令
netstat -tuln
    -t：仅显示TCP协议的端口。
    -u：仅显示UDP协议的端口。
    -l：仅显示监听状态的端口。
    -n：直接使用IP地址而不是域名。



#查看可以登录的用户
cat /etc/passwd | grep bash



#打包网站所有内容
tar -cvf web.tar /var/www/html  #这个命令会将 /home/kali 文件夹及其所有内容打包到web.tar文件中。


打开D盾，查杀websehll


关闭shell连接进程
终端输入：who
会提示已经登录进来的账户
```

![image-20230413143738191](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230413143738191.png)

```
如果IP地址和上面显示不一致，就要将他踢掉
踢掉方式：pkill  kill -t pts/2
```

![image-20230413144133755](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230413144133755.png)

```
find ./ -cmin -10
```

![image-20230413144643191](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230413144643191.png)





```
删除不死马
```

```
利用脚本，在后台不断查杀不死马

vim killshell.sh
chmod 777 killshell.sh
nohup ./killshell.sh &

#!/bin/bash
while true
      do
           rm -rf  xx.php
      done
      
查看脚本文件
ps aux | grep killshell.sh
```



```
发现网站有漏洞，直接echo一个空值就行

echo   >  xxx.php
```

