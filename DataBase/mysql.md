
显示数据库列表：`show databases;`

打开某个数据库：`use 库名`

显示库列表：`show tables;`

显示数据表结构：`desc 表名`

创建数据库：`create database 库名`

建表：`create table 表明(字段设定列表)`

删库删表：`drop database 库名` `drop table 表名`

导出数据库： `mysqldump -u root -p 库名 > sql文件名`

***

创建时间：CURRENT_TIMESTAMP
修改时间：ON UPDATE CURRENT_TIMESTAMP

建库时使用中文字符集：`CREATE  DATABASE 数据库名 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;`


### MySQL 5.7.21-1 安装后密码正确无法登录

MySQL Server version: 5.7.21-1 (Debian)

安装之后没有提示设置 root 用户密码，无法登录，无奈只好修改配置文件过权限表认证：

` sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf ` 在 `[mysqld]` 中添加： `skip-grant-tables`

- 进入 MySQL ，修改 `user` 表中的 `authentication_string` 字段

`update user set authentication_string = password('root') where user = 'root' ;`

- 更新：
`flush privileges;`

密码设置为 `root` 之后，还是无法登录！最后发现，`user` 表中有一个字段是：`plugin` 将他修改为 `mysql_native_password` 即可登录：

`update user set plugin = 'mysql_native_password where user = 'root'; `
最后，还要记得更新！


### 中文排序
`SELECT * FROM sqllearn.Orders ORDER BY orderNumber DESC, convert(company using gbk)` 需要使用 `convert` 转换
