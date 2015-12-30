Bash Userc
==========

Bash 的用户自定义配置。

### 使用方法

将 userc 文件拷贝到 ～/ 目录下并重命名为 .userc，然后在 ~/.bashrc 中添加如下内容

```
if [ -f ~/.userc ]; then  
    . ~/.userc  
fi
```
