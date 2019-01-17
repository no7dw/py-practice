### pylint 

问题：
打开py 文件 提示 vscode "Path to the pylint linter is invalid" 
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pylint
或者提示：
vscode "Path to the pylint linter is invalid"

原因：
pylint 未安装、配置正确：

解决：
pip show pylint 看看版本
settings.json  设置成这样就好了

```
  "python.linting.pylintPath": "pylint",
  "python.pythonPath": "/usr/bin/python3",
```

[使用vscode开发Python程序：代码静态检查工具pylint及代码格式化工具yapf的配置使用](https://blog.csdn.net/sunxb10/article/details/80984243)
[Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)


### vscode 下python 命令行版本不对

```
  which -a python3
```
选择正确的版本然后fill 到对应 settings.json 的 pythonpath

# ImportError: cannot import name
  [dep](https://segmentfault.com/a/1190000010600365)
  [name & dep](https://blog.csdn.net/m0_37561765/article/details/78714603)

# bad magic number error
  [stackoverflow](https://stackoverflow.com/questions/514371/whats-the-bad-magic-number-error)
  [pyc](https://blog.csdn.net/kmust20093211/article/details/41649929)

  

# Python  SyntaxError: Non-ASCII character '\xe5' in file
文件最开头加入一行
```
  # -*- coding: UTF-8 -*-
```
or
```
  #coding=utf-8
```


[Python“Non-ASCII character 'xe5' in file”报错问题](https://blog.csdn.net/geekmanong/article/details/50514984)