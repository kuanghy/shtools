Windows 子系统配置
========

## 操作命令

```
# 列出所有安装的版本
wsl --list --verbose

# 设置默认体系为 wsl2
wsl --set-default-version 2

#终止所有 WSL 实例
wsl --shutdown
```

## 开机自动启动服务

在 Windows 中使用 `Win + R` 搜索并打开 `shell:startup` 进入启动目录，将 Ubuntu.vbs 文件移动至该目录

在 wsl 中将 init.wsl 移动至 /etc 目录中

## 磁盘挂载等配置

将 wsl.conf 拷贝到 /etc/wsl.conf

## 解决内存占用问题

在 Windows 的用户目录创建 .wslconfig 文件，添加如下内容：

```
[wsl2]
processors=8
memory=8GB
swap=8GB
localhostForwarding=true
```

添加 crontab 清除缓存：

```
# Clear system cache
*/30 * * * * root sync; echo 3 > /proc/sys/vm/drop_caches; date > /tmp/drop_caches_last_run
```


*Copyright (c) Huoty, 2021.02.05*
