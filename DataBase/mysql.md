
显示数据库列表：`show databases;`

打开某个数据库：`use 库名`

显示库列表：`show tables;`

显示数据表结构：`desc 表名`

创建数据库：`create database 库名`

建表：`create table 表明(字段设定列表)`

删库删表：`drop database 库名` `drop table 表名`

***

创建时间：CURRENT_TIMESTAMP
修改时间：ON UPDATE CURRENT_TIMESTAMP

建库时使用中文字符集：`CREATE  DATABASE 数据库名 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;`
