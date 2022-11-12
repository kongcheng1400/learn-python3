#

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

```