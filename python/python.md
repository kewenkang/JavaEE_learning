### 一、 python的数据结构

1. hashmap  ->  dict
    dict = {"red": 1, "green": 2, "blue": 3}
    dict.get("red") 返回1，若没有则返回None
    dict.pop("red") 删除"red"
    for value in dict.values() 获取所有的value, key不用获取直接用key in dict
    for k, v in dict.items() 获取所有的键值对
2. array  ->  list
    注：字符串也是数组
    list = ["ww", "qq", "ee", "rr"] 
    list.append("dd")
    list.insert(index, value)
    list.pop(index) 默认删除尾部元素
3. set  ->  set
    c_set = set()
    c_set.add("www")
    c_set.add("eee")
    c_set.remove("www")

---
### 二、 分支结构 注注注：python所有的分支结构后面都要加 **冒号**

1. if...else
    a=2
    if a>0:
        print 1
    elif a==0:
        print 0
    else :
        print -1

2. for循环
    for value in list:
        print value

    sum = 0    
    for value in range(1, 11):
        sum += value
    print sum

3. while循环
    i = 1
    while i < 10:
        i += 1
        if i % 2 =0:
            print i

    while i > 1:
        i -= 1
        if i % 5 == 0:
            break  # continue
        print i

#### 字符串 str='AbcdefG'

1. len(str)  # 7  输出字符串，字典，set的长度
2. str[2: 5]   # cde  起始位置和结束位置
3. str.lower()  # abcdefg  转为小写

---
### 三、 python高级特性

1. 切片
2. 迭代
    isinstance([1,2], Iterable) 判断是否可迭代
    for index, val in enumerate([1,2,3]) enumerate()将list变成索引-元素对
3. 列表生成式
    [x*y for x in [1,2,3] for y in [-1,-2,-3] if x%2 == 1]
4. 生成器(generator.py)
    将列表生成式的[]改为()
    g = (x*x for x in range(1, 10))
    next(g) 获取生成器的下一个元素
    for n in g 

    注：
    * 在函数中使用yield，函数就变成了生成器；
    * 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
5. 迭代器
    生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

    把list、dict、str等Iterable变成Iterator可以使用iter()函数
    把Iterator变成list可以使用list(iterator)

---
### 四、 python函数式编程

1. 高阶函数(mrfs.py)
    1. map(fn, iterable)  reduce(fn, iterable)
    2. filter(fn, iterable)  Iterator经过filter后会变成Iterable
    3. sorted(iterable, key=xx, reverse=True)
2. 返回函数
3. 匿名函数
    lambda x: x*x
4. 装饰器(decorator.py)
5. 偏函数
    functools.partial(func, **kw)


---
### 五、 错误、调试和测试

1. 异常处理 try .. except ... finally
    + logging.exception(e) #打印异常堆栈
    + raise ValueError("xxxx") #抛出异常
    + except Exception as e: #捕获异常

        try:
            b = 3 / 0
        except Exception, e:
            print Exception, ":", e

        try:
            print "1111"
            fh = open("testfile", "r")
            print "2222"
        except IOError, e:
            print "3333:", e
        else:
            print "4444"
            fh.close()

2. 调试
    + 断言 assert
        - assert n != 0, "n is zero"
        - 启动Python解释器时可以用-O参数来关闭assert
    + logging
        - import logging
        - 设置logging的级别,级别低的会覆盖级别高的 logging.basicConfig(level=logging.INFO)
            * debug(4)
            * info(3)
            * waring(2)
            * error(1)    

---
### 六、 python IO

1. 文件读写
    - f = open("fileName", 'r')
    - with open('fileName', 'r') as f: #会自动关闭文件
2. StringIO 内存中读写str
    from io import StringIO
    f = StringIO() 或 StringIO("hello")
    f.write("xxx")
    f.getvalue() 
    s = f.readline()
3. BytesIO 内存中读写bytes
    from io import BytesIO
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
4. 操作文件
    - import os
    - os.name #操作系统类型
    - os.uname() #详细的系统信息，可以调用uname()函数
    - os.environ #在操作系统中定义的环境变量
    - os.path.abspath('.') # 查看当前目录的绝对路径
    - os.path.join('/Users/michael', 'testdir') # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    - os.path.append('')
    - os.mkdir('/Users/michael/testdir')
    - os.rmdir('/Users/michael/testdir')
    - os.path.split('/Users/testdir/file.txt') #把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
      ('/Users/michael/testdir', 'file.txt')
    - os.path.splitext()可以直接让你得到文件扩展名
    - os.rename('test.txt', 'test.py')
    - os.remove('test.py')
    - shutil模块提供了copyfile()的函数,还可以在shutil模块中找到很多实用函数
    
    - os.listdir('.')
    - os.path.isdir(x)
    - os.path.isfile(x)

5. 序列化
    1. pickle模块
        + import pickle
        + pickle.dumps(obj)方法把任意对象序列化成一个bytes
        + pickle.dump(obj, file)直接把对象序列化后写入一个file-like Object
        + pickle.loads(bytes)方法反序列化出对象
        + pickle.load(file) 从一个file-like Object中直接反序列化出对象
    2. JSON 
        + import json
        + json.dumps(obj)方法把任意对象转化为标准json字符串
        + json.dump(obj, file)
        + json.loads(json_str)
        + json.load(file)
        + json.dumps(obj, default=lambda obj:obj.__dict__) 将class对象序列化（含__slots__不可）
        + json.loads(json_str, object_hook=dict2student) 将json字符串转为class对象

### python模块

---
### 七、 python面向对象编程

1. __slots__ = ('name', 'age') 限制动态地绑定属性，但是对子类无效
2. __len__(self) 方法我们也知道是为了能让class作用于len()函数
3. __str__(self) print对象s时，会自动调用str(s)
4. __repr__(self) 直接打s，会调用repr(s)输出s的地址，用于调试
5. __iter__(self),__next__(self) 
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
6. __getitem__(self, n) 让对象向数组一样可以通过下标取值；对切片对象slice要单独做判断
7. __getattr__(self, attr) 只有当调用的属性不存在时，才会调用该方法来尝试获得属性
8. __call__(self) 对象实例s，调用s()时会自动调用call方法；判断一个对象是否能被调用即有无__call__，callable(Student())
2. @property 相当于@attr.getter
3. @attr.setter 
4. 枚举类型（enum.py）


### 导入module
```python
    import math
    import random
    
    print math.pow(2,3)  # 8
    print math.floor(4.9)  # 4.0
    print round(4.9)  # 5.0

    items = [1,2,3,4,5,6]
    random.shuffle(items)
    sam = random.sample(items, 3)  # 随机抽样 3个
    print items  # 3,2,4,1,5,6    
    print sam

    a = random.randint(0, 3) # 0-3间的随机数


```    
