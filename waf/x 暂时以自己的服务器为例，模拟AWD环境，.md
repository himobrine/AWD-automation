```
暂时以自己的服务器为例，模拟AWD环境，
```

### 防守阶段

```
下载网站目录，也就是打包网站备份
```

```
部署文件监控脚本
```

这里如果没有python环境的话，直接用linux的脚本

![image-20230408132039755](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408132039755.png)

将文件上传到服务器任意位置就行

然后运行

![image-20230408132151695](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408132151695.png)

```
waf脚本部署，在index.php里面包含waf脚本
或者在任何感觉存在漏洞的位置包含这个waf脚本
```

![image-20230408135152602](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408135152602.png)

```
这个脚本会生成一个/tmp/1log的日志文件
```

![image-20230408135335420](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408135335420.png)

![image-20230408135717661](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408135717661.png)

```
这五个日志文件分别对应：（最主要是第二个日志数据）
黑客访问的data数据包
访问的数据包，get和post请求
详细的数据包
```

```
如果，网站存在命令执行漏洞，攻击者执行cat flag
```

![image-20230408140308867](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140308867.png)

![image-20230408140321454](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140321454.png)





```
禁止ip访问页面脚本
```

![image-20230408140501925](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140501925.png)

```
也是和WAF脚本一样，文件包含一下这个脚本
```

![image-20230408140637624](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140637624.png)

```
然后呢，直接编辑这个脚本文件，如果是黑客ip，直接填写就行，也就相当于拉黑
```

![image-20230408140831090](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140831090.png)

```
拉黑之后，是访问不到页面的
```

![image-20230408140919970](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408140919970.png)





```
如果对方部署了WAF脚本，就用搅屎棍脚本，基于python3的脚本
```

![image-20230408141218411](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408141218411.png)





```
ip存活探测脚本，这里是举个例子
```

![image-20230408141450581](C:\Users\bbaig\AppData\Roaming\Typora\typora-user-images\image-20230408141450581.png)



### SSH密码修改:

```
passwd
```

### mysql密码修改:

```
#方法一
show databases;
use mysql
set password for root@localhost = password('123');
#方法二
update user set password = PASSWORD('需要更换的密码') where user='root';
flush privileges;
show tables;
```

### 目录打包

```
打包
tar -zcvf archive_name.tar.gz  directory_to_compress
注意：如果使用tar命令打包文件夹，.index.php（隐藏类型文件）将不会被打包

备份整站
cd /var/www && tar -czvf /tmp/html.tgz html
# 软连接到了/app
cd / && tar -czvf /tmp/app.tgz app

解包
tar -zxvf archive_name.tar.gz
```

### 2.备份数据库

- 备份指定的多个数据库

```
mysqldump -uroot -proot --databases DB1 DB2 > /tmp/db.sql
```

无 lock tables 权限的解决方法

```
mysqldump -uroot -proot --all-databases --skip-lock-tables > /tmp/db.sql
```

- 恢复备份（在 MySQL 终端下执行）

```
source FILE_PATH
```
