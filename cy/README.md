### hello world

python3 setup.py build_ext --inplace
Compiling test.py because it changed.
[1/1] Cythonizing test.py
running build_ext
building 'test' extension
creating build
creating build/temp.macosx-10.7-x86_64-3.7
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/anaconda3/include -arch x86_64 -I/anaconda3/include -arch x86_64 -I/anaconda3/include/python3.7m -c test.c -o build/temp.macosx-10.7-x86_64-3.7/test.o
gcc -bundle -undefined dynamic_lookup -L/anaconda3/lib -arch x86_64 -L/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.7-x86_64-3.7/test.o -o /Users/dengwei/projects/github/no7dw/py-practice/cy/test.cpython-37m-darwin.so


dengwei@RMBAP:~/projects/github/no7dw/py-practice/cy$ mv test.py test1.py

dengwei@RMBAP:~/projects/github/no7dw/py-practice/cy$ python3
Python 3.7.1 (default, Dec 14 2018, 13:28:58)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import test
>>> test.say_hello()
hello world

### 效果测试

看测试bench.py ，纯python运行 13.7s , cython 优化后8.4s, 提升 30%+

>>> 8.408564805984497-13.719650745391846
-5.311085939407349
>>> -5.311085939407349/13.719650745391846
-0.38711524352697063
