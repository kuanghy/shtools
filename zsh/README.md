Oh my zsh 配置参考
==================

## 主题安装

拷贝 konyon.zsh-theme 或者 konyonm.zsh-theme 到 oh-my-zsh 主题目录，如 ~/.oh-my-zsh/custom/themes 或者只做软连接，然后修改主题配置项：

```
ZSH_THEME="konyon"
```

设置本地与 ssh 登录用不同的主题：

```
if [[ -n $SSH_CONNECTION ]]; then
    export ZSH_THEME='konyonm'
else
    export ZSH_THEME='konyon'
fi
```

## 配置参考

```
# 大小写不敏感
CASE_SENSITIVE="true"

# 连接符不敏感，否则 _ 和 - 将可以互换
HYPHEN_INSENSITIVE="true"

# 自动纠正命令
ENABLE_CORRECTION="true"

# 按 tab 键补全命令的时候
# 如果没什么可补全的就会出现三个红点，更人性化显示
COMPLETION_WAITING_DOTS="true"

# 历史命令日期显示格式
# 有三种方式: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="yyyy-mm-dd"

# 别名
alias zshconfig="vi ~/.zshrc"
alias ohmyzsh="cd ~/.oh-my-zsh"
alias reload-zshrc="source ~/.zshrc"
```

## 插件推荐

- **sudo**

敲两下 esc 自动在命令前边加上 sudo

- **z**

加载 [z.sh](https://github.com/rupa/z), 用于快速跳转到常用目录

- **extract**

智能判断压缩包后缀来选择解压命令，输入 x 命令就可以解压所有文件

- **osx**

一款增加了一些在OSX上实用的命令插件:

```
tab - 在一个新标签打开当前目录
cdf - cd到当前Finder目录
quick-look - 快速浏览特殊的文件
man-preview - 在Preview应用打开特定的man page
trash - 将特定的文件移到垃圾桶
```

- **urltools**

对 url 进行编码:

> urlencode http://wdxtub.com

对 url 进行解码:

> urldecode http%3A%2F%2Fwdxtub.com

- **python**

Python 参数补全， `pyfind` 查找当前目录下的 Python 文件，`pyclean` 清理当前目录下的 Python 二进制文件和缓存文件， `pygrep` 在 Python 文件中查找字符串

- **docker**

Docker 参数补全

- **supervisor**

Supervisor 参数补全


- **zsh-syntax-highlighting**

高亮常用命令，安装：

> git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

- **zsh-autosuggestions**

命令建议提示，安装

> git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions