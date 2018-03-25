Compare Python with Node.js

all Node.js knowledge is in ()
# basic
- list (array)
	- method:insert() /pop()

	>>> namelist = ['Deng', 'Wei']
	>>> namelist[0]
	'Deng'
	>>> namelist[1]
	'Wei'
	>>> namelist[2]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: list index out of range
	>>> namelist[-1]
	'Wei'

- tuple (more than **const array**  --- Object.freeze)

	>>> nametuple=('Deng','Wei')
	>>> nametuple[0]
	'Deng'
	>>> nametuple[2]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: tuple index out of range
	>>> nametuple[-1]
	'Wei'
	>>> nametuple[-1]='Wei2'
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

- 	dict (json key-value)
	
	>>> IDNamedict={'001':'dengwei','002':'david','003':'wade'}
	>>> IDNamedict['001']
	'dengwei'
	>>> IDNamedict['004']
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: '004'

- 	set(Set)
- 	generator(generator)
- 	isinstance/type(type of)
 	
	>>> isinstance(namelist,list)
	True
	>>> isinstance(namelist,tuble)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'tuble' is not defined
	>>> isinstance(namelist,tuple)
	False
	>>> type(namelist)
	<class 'list'>
	>>> type(namelist) is list
	True

# class
- inheritance(father) (vs extends)
	
	class Bird(Animal):
	    pass

- multiple inheritance(mixin： Object.assign(obj.prototype,mixin   [mixwith.js](https://github.com/justinfagnani/mixwith.js))) 
	
	class MyUDPServer(UDPServer, ThreadingMixIn):
	    pass

# package install
- https://pypi.python.org (npmjs.org)
- install command: easy_install/pip (npm )
- pip3 install -r requirements.txt (npm i)
    -  pip3 install gunicorn (npm install lodash)
# unittest
- package 
	-  unitest(mocha)	-- internal package
		- run command
		    - $python3 test_xx.py 
		        - 留意
		            - 名字命名要 以test_ 开头，class 内的函数 以 test_xx 开头
		            - class TestXXX(unittest.TestCase)
		    - $python3 -m unittest discover test # test 目录自发现
		    - mock(nock)
		
			from mock import MagicMock
			thing = ProductionClass()
			thing.method = MagicMock(return_value=3)
			self.assertEqual(thing.method(), 3)
	- py.test(mocha)  -- 3rd testing framework
		- run command
			
			py.test
		- test case
			
			- 使用 @pytest.mark.parametrize 初始参数化test case 的参数
			- 使用 (teardown_class/teardown_module、setup_class/setup_module)[https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown]	 来做准备工作&销毁工作


# decorator
- some only in ts

# important internal package

# import 3rd package

# data processing
- package
	- pydash(lodash)
	- panda(more than mathjs)

# async 
- async/await(async/await)
	- package
		-  asyncio
		-  aiohttp
		-  threading

# db
- package
	-  mysql-connector-python/mysql-connector(sequelize)
	-  pymongo(mongoose)
	
# web framework:
- flask(expressjs) 
    - [demo](https://github.com/no7dw/py-practice/tree/master/flask-demo)
    - FLASK_DEBUG=1 FLASK_APP=hello-world.py flask run (node-dev/nodemon)# auto reload 
    - 

from python2.7 to python3
	causion: may need to handle somelib version change

	`
		2to3 2.py -w 
	`