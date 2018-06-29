源码编译安装 MySql
================

## 下载源码

> wget http://mirrors.sohu.com/mysql/MySQL-5.7/mysql-5.7.18.tar.gz

## 编译

```
cmake \
-DCMAKE_INSTALL_PREFIX=~/.local/mysql \
-DMYSQL_DATADIR=~/.local/mysql/data \
-DSYSCONFDIR=~/.local/mysql/etc \
-DMYSQL_UNIX_ADDR=~/.local/mysql/tmp/mysql.sock \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DMYSQL_TCP_PORT=33306 \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_PARTITION_STORAGE_ENGINE=1 \
-DEXTRA_CHARSETS=all \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci \
-DDOWNLOAD_BOOST=1 \
-DWITH_BOOST=./boost/boost_1_59_0


make -j 4 && make install
```

## 创建配置文件

创建 my.cnf 配置文件，并配置相应选项

## 初始化

> ./bin/mysqld --defaults-file=my.cnf --initialize --console

## 启动

> ./bin/mysqld_safe --defaults-file=my.cnf

## 登录数据库

> ./bin/mysql -h localhost -P 33306 -u root -S run/mysqld.sock -p

在日志文件中有临时密码，首次登陆之后需要先修改密码：

```
SET PASSWORD = PASSWORD('new_password');
```

MySQL8 之后使用如下方式修改 root 密码：

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
```

## 创建数据库

> create databases dev;

导入数据：

```
mysql -u 用户名 -p  数据库名 < 数据库名.sql
mysql -u abc -p abc < abc.sql
```