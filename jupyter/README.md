Jupyter 相关的配置
========

安装配置文件：

```
cp ipython_config.py ~/.ipython/profile_default/
cp startup-00-init.py ~/.ipython/profile_default/startup/00-init.py
```

安装内核：

```
python2 -m pip install ipykernel
python2 -m ipykernel install --user

python3 -m pip install ipykernel
python3 -m ipykernel install --user
```


*Copyright (c) Huoty, 2021.11.03*
