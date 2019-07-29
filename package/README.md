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

当然也可以在作为git 项目直接upload 到git repo，然后再git clone 去分发

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


### pip install 

    可以按照直接是git的地址 
    pip install https://github.com/ilex/aiomotorengine/archive/master.zip

### Error FAQ

   安装包的时候，需要扫描需要的依赖, 使用pip freeze > requirements.txt
   但他包含了很多当前项目不需要的依赖
   因此使用以下方法简化：

```
    pip(3) install pipreqs
    #then
    pipreqs path/to/project
```
    
    另外有时：requirements.txt 里面的依赖包版本可能找不到或者报错，我们需要忽略错误的时候，pip 没有提供ignore-error 之类的选项
    使用以下方法进行逐个安装解决：

```
    cat requirements.txt | xargs -n 1 pip install
```

