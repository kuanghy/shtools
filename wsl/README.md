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


*Copyright (c) Huoty, 2021.02.05*
