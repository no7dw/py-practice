### cython hello world

步骤：

  - edit test.py 作为hello world 简版
  - 用distutils setup搞成包
  - 即可在python3 里面 import 使用

python3 setup.py build_ext --inplace
Compiling test.py because it changed.
[1/1] Cythonizing test.py
running build_ext
building 'test' extension
creating build
creating build/temp.macosx-10.7-x86_64-3.7
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/anaconda3/include -arch x86_64 -I/anaconda3/include -arch x86_64 -I/anaconda3/include/python3.7m -c test.c -o build/temp.macosx-10.7-x86_64-3.7/test.o
gcc -bundle -undefined dynamic_lookup -L/anaconda3/lib -arch x86_64 -L/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.7-x86_64-3.7/test.o -o /Users/dengwei/projects/github/no7dw/py-practice/cy/test.cpython-37m-darwin.so



  #移除掉源文件，以免影响
  dengwei@RMBAP:~/projects/github/no7dw/py-practice/cy$ mv test.py test1.py
  dengwei@RMBAP:~/projects/github/no7dw/py-practice/cy$ python3
  Python 3.7.1 (default, Dec 14 2018, 13:28:58
  [Clang 4.0.1 (tags/RELEASE_401/final] :: Anaconda, Inc. on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import test
  >>> test.say_hello(
  hello world

### benchmark效果测试

看测试bench.py ，纯python运行 13.7s , cython 优化后8.4s, 提升 30%+

  >>> 8.408564805984497-13.719650745391846
  -5.311085939407349
  >>> -5.311085939407349/13.719650745391846
  -0.38711524352697063

### 其他方法
不使用python + cython setup 方式编译的话，可以参考这里 
[Compile main Python program using Cython](https://stackoverflow.com/questions/5105482/compile-main-python-program-using-cython
但 过程需要注意自己gcc， 注意 -I 对应的include 头文件 ，ld 对应的lib。比较麻烦，并且要最好弄个virtual env 来搞。

### 多个文件夹/包的处理

```
  from distutils.core import setup
  from Cython.Build import cythonize

  setup(
      ext_modules = cythonize(["folder1/file1.py", "folder2/file2.py"])
  )
```

[Cython的用法以及填坑姿势](https://blog.csdn.net/feijiges/article/details/77932382
[Creating an executable file using Cython](http://masnun.rocks/2016/10/01/creating-an-executable-file-using-cython/)
[Cython docs](http://docs.cython.org/en/latest/src/quickstart/build.html)
[Cython setup.py for multiple .py and multiple folder](https://stackoverflow.com/questions/21826137/cython-setup-py-for-several-pyx)