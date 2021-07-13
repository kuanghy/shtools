Shell Tools
===========

Shell 工具集，包含一些命令行实用的脚本，shell 配置，工具软件配置等，如 apache、nginx、mysql、supervisor、tmux、zsh 等的配置示例。

部分配置和脚本的使用说明：

- **shrc**

用于增强 shell 配置，包括 **一些命令 alias 和 函数库**，便于日常工作。配置兼容 Bash 和 Zsh，兼容 Linux、Mac OS X 以及 Cygwin、Git Bash。在 ~/.bashrc 或者 ~/.zshrc 中载入 shrc 配置即可:

```shell
if [ -f ~/.shrc ]; then
    . ~/.shrc
fi
```

需要将 shrc 文件拷贝到 ~/ 目录下并重命名为 .shrc，可直接下载：

```shell
wget https://gitee.com/konghy/shtools/raw/master/shrc -O ~/.shrc

# 或

curl https://gitee.com/konghy/shtools/raw/master/shrc -o ~/.shrc
```


配置中包含几个简单的 bash 提示符样式，如果需要修改命令提示符样式，可以在做如上引入之后，在 `~/.bashrc` 文件中添加如下内容:

```
# custom command prompt style
export PS1=$SCHEME4
```

- **gitconfig**

**Git 配置文件**。如果作为全局使用，则拷贝到主目录下：

```shell
curl https://gitee.com/konghy/shtools/raw/master/gitconfig -o ~/.gitconfig
```

如果作为项目配置文件，则拷贝到项目目录，并重命名为 `.gitconfig`.

- **bashrc_docker**

**一些 docker 命令的 alias**。将 bashrc_docker 文件拷贝到 ～/ 目录下并重命名为 .bashrc_docker，然后在 ~/.bashrc 中添加如下内容

```shell
if [ -f ~/.bashrc_docker ]; then
    . ~/.bashrc_docker
fi
```

- **tmux**

从 tmux 目录下选择合适的配置文件拷贝到 ~/.tmux.conf，如：

```shell
curl https://gitee.com/konghy/shtools/raw/master/tmux/k-local3.conf -o ~/.tmux.conf
```

设置 Tmux 自动补全，在 ~/.bashrc 中添加如下内容以增强对 tmux 的补全功能：

```shell
if [ -f ~/shtools/tmux/bash_completion_tmux.sh ]; then
    source ~/shtools/tmux/bash_completion_tmux.sh
fi
```
