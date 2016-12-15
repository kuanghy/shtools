Bash Tools
==========

Bash 工具集

## userc

**一些命令 alias 和 函数库**，便于日常工作。将 userc 文件拷贝到 ～/ 目录下并重命名为 .userc，然后在 ~/.bashrc 中添加如下内容

```
if [ -f ~/.userc ]; then  
    . ~/.userc  
fi
```

如果需要修改命令提示符样式，可以在做如上引入之后，在 `~/.bashrc` 文件中添加如下内容:

```
# custom command prompt style
export PS1=$SCHEME4
```

## gitconfig

**Git 配置文件**。如果作为全局使用，则拷贝到主目录下：

> mv gitconfig ~/.gitconfig

如果作为项目配置文件，则拷贝到项目目录，并重命名为 `.gitconfig`

## bashrc_docker

**一些 docker 命令的 alias**。将 bashrc_docker 文件拷贝到 ～/ 目录下并重命名为 .bashrc_docker，然后在 ~/.bashrc 中添加如下内容

```
if [ -f ~/.bashrc_docker ]; then  
    . ~/.bashrc_docker  
fi
```

## 设置 Tmux 自动补全

在 ~/.bashrc 中添加如下内容以增强对 tmux 的补全功能：

```
if [ -f ~/aboutme/bash-tools/tmux/bash_completion_tmux.sh ]; then
    source ~/aboutme/bash-tools/tmux/bash_completion_tmux.sh
fi
```


## ressh

**登陆远程服务器**。自动化 ssh 连接远程服务器，需要安装 `autossh` 和 `expect`:

> sudo apt-get install autossh
> 
> sudo apt-get install expect

远程主机地址和密码等信息需保存在环境变量中，脚本通过读取环境变量获取相应信息以实现自动登录。可以把环境变量写在 `~/.bashrc` 文件中：

```
export R_HOST="192.168.1.118"
export R_USER="huoty"
export R_PASS="181716"
export R_PORT="23456"
```

这样就不必每次都设置环境变量，只有在需要的时候再修改相应的值，例如换其他的用户名登录则重设 `R_USER` 变量。`R_PORT` 为端口号，不设置时表示使用默认的端口号。脚本支持添加额外的 ssh 参数。

**注意：**，这个脚本有一个缺陷，如果是第一次连接服务器，由于无法保存服务器指纹文件，脚本会出错。解决方法很简单，先手动连接一次就可以了。
