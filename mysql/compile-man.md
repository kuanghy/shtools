Դ����밲װ MySql
================

## ����Դ��

> wget http://mirrors.sohu.com/mysql/MySQL-5.7/mysql-5.7.18.tar.gz

## ����

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

## ���������ļ�

���� my.cnf �����ļ�����������Ӧѡ��

## ��ʼ��

> ./bin/mysqld --defaults-file=my.cnf --initialize --console

## ����

> ./bin/mysqld_safe --defaults-file=my.cnf

## ��¼���ݿ�

> ./bin/mysql -h localhost -P 33306 -u root -S run/mysqld.sock -p

����־�ļ�������ʱ���룬�״ε�½֮����Ҫ���޸����룺

```
SET PASSWORD = PASSWORD('new_password');
```

MySQL8 ֮��ʹ�����·�ʽ�޸� root ���룺

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
```

## �������ݿ�

> create databases dev;

�������ݣ�

```
mysql -u �û��� -p  ���ݿ��� < ���ݿ���.sql
mysql -u abc -p abc < abc.sql
```