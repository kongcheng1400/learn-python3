# Python3 错误和异常

## try/except
异常捕捉:
```python
try:
    exceutioncode
except xxxError: #except (RuntimeError, TYpeError, NameError):
    异常执行
else:
    没有异常时执行
finally:
    不管又没有异常
```



```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except: #捕获所有异常，向上提交
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

## try/except...else
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### raise
```python
>>> try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise
   
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in ?
NameError: HiThere

```

### 自定义异常

```python
>>> class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
   
>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
   
My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```

#### 最简单的自定义异常:
```python
class SimplestError(Exception): pass
raise SimplestError('simplest error from %s at %d' % ('testdemo', 1))
#SimplestError: simplest error from testdemo at 1
```

### with
- with封装了try...except...finally
- 在处理文件对象时使用with关键字时一种很好的做法


不使用with，也不使用try...except...finally
```python
file = open('./test_runoob.txt', 'w')
file.write('hello world !')
file.close()
```
假设wrte中有异常:
```python
file = open('./test_runoob.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()
```

使用with:
```python
with open('./test_runoob.txt', 'w') as file:
    file.write('hello world !')
```

使用原理:

