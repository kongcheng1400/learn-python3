# class
- 类成员通常为public, 所有成员函数都是virtual
## class 对象.
类对象支持两种操作，属性引用和实例化.
实例对象的操作: 属性引用。数据属性和方法。

### 类变量和实例变量:
这个类变量不是很明显:
```python
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

## oop

- __init__(): 构造方法.
- self代表类的实例:
- 类方法与普通的函数的区别：它们必须有一个额外的第一个参数名称，按照惯例是self
- __private_attrs:两个下划线开头，声明该属性为私有.
- __private_method:私有方法.


```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
```

类的方法:
```python
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()
```



```python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```
#### 继承:
```python
#类定义
class People:
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
s = student('ken',10,60,3)
s.speak()
```

## 模块
`import modulename`
`from modulename import name1[, name2]`
`from modulename import *`
`dir(modulename)`

example1:
```python
import sys
print(sys.path)
dir(sys)
```

example2:
```python
from fibo import fib, fib2
fib(500)
```

### 包
管理python模块命名空间:采用 packagename.modulename

## 输入和输出
- print()
- str(x)
- repr(): 可以是python任何对象.
- str.format()



```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # 注意前一行 'end' 的使用
...     print(repr(x*x*x).rjust(4))
 1   1    1
 2   4    8
 3   9   27
 4  16   64
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
```
- 每列之间的空格由`print()`添加.
- `rjust()`:将字符串靠右
- `str.zfill(n)`:给数字左边填0

### str.format()
- 括号机器里面的字符(格式化字段)将会被format()中的参数替换.

```python
>>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
菜鸟教程网址： "www.runoob.com!"
>>> print('{0} 和 {1}'.format('Google', 'Runoob'))
Google 和 Runoob
>>> print('{1} 和 {0}'.format('Google', 'Runoob'))
Runoob 和 Google

# 使用关键字参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
菜鸟教程网址： www.runoob.com

# !a，!s, !r
>>> import math
>>> print('常量 PI 的值近似为： {}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
>>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。

# 可选项:和格式标志符:更好的格式化
>>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
常量 PI 的值近似为 3.142。

# :后跟着一个数字，则是最少宽度，用于美化表格
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> for name, number in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, number))
...
Google     ==>          1
Runoob     ==>          2
Taobao     ==>          3
```

### 使用%格式化.

```python
>>> import math
>>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
常量 PI 的值近似为：3.142。
```

## 文件读写
`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
`
```
# 打开一个文件
f = open("/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

```

### 文件对象
- `f.read()`

## os
