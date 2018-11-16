# python 如何编写一个自己的包  

### 先写function 内容

    package/wadepypk$ ls
    __init__.py f1.py       f2.py

f1.py

```
    def show():
        print("in pkg f.show()")
```

f2.py

```
    def show():
        print("in pkg f.show()")
```

__init__.py

```
    __all__ = ['f1','f2']
```

上层目录建立一个setup.py

```
    from distutils.core import setup

    setup(
            name='wadepypk',
            version='1.0',
            description='This is a test of the setup',
            author='huoty',
            author_email='no7david123@gmail.com',
            url='https://www.deng.io',
            packages=['wadepypk']
    )
```

### build

    python setup.py build

### 打包

    python setup.py sdist

得到一个wadepypk-1.0.tar.gz

### 使用

    tar -zxvf wadepypk-1.0.tar.gz
    cd wadepypk-1.0
    python setup.py install

则安装到本地的目录里面 

python具体代码调用 

```
>>> from wadepypk import f1,f2
>>> f1.show()
in pkg f.show()
>>> f2.show()
in pkg f.show()
```

### 升级包

修改下源码
f2.py

```
    def show():
        print("in pkg f2.show()")
```

重新 build, sdist ,install ,setup

退出python 终端，不然仍然使用cache 里面的1.0包版本

```
    >>> from wadepypk import f1,f2
    >>> f2.show()
    in pkg f2.show()
```

原来的"in pkg f.show()" 已经改为 "in pkg f2.show()"

