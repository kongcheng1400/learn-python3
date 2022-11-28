# 基本数据类型

内置的标准类型:
- number(int, float, complex)
  - bool是int的子类，唯一实例就是False, True
- 迭代器类型/容器类型.
- 序列:list, tuple, range
- map
- class
- instance
- except(异常)

容器类型: lsit, set, tuple, dict

## int类型的附加方法.
int.bit_length()
int.bit_count()
int.to_bytes()
int.from_bytes(bytes, byteorder='big', *, signed=False)
int.as_integer_ratio()

## float类型的附加方法
float.as_integer_ratio()
float.is_integer()

## 迭代器类型，迭代协议，容器
container.__iter__()返回迭代器对象.
迭代器协议: iterator.__iter__(), iterator.__next__() 支持这两个方法.
迭代完成则返回StopIteration异常.

## 生成器类型--实现迭代器协议的便捷方式.

## 序列及通用序列操作
- 三种基本序列: list, tuple, range.
- 基本运算
  - `x in s`
  - `x not in s`
  - `s + t`
  - `s[i:j:k]`切片
  - len(s)
  - min(s)
  - max(s)
### 可变序列 操作
- s[i] = x

## slice 对象
- range返回slice对象
- 扩展索引语法: a[start:stop:step]或者a[start:stop, i]
list: [e,e,e]
tuple: (e,e,e)
set: {}


```
a, b, c, d = 1, 3.3, True, 4+3j
print(type(a), type(b), type(c), type(d))
isinstance(a, int)
```
`type()`和`isinstance()`的区别: isinstance()会认为子类是一种父类类型
`bool`是`int`的子类

- 直接赋值对象才被创建
- 使用`del`来删除


## List
- class list([iterable])
- 序列是python中最基本的数据结构
### 创建列表
- 空列表[]
- 方括号，逗号分隔[a],[a,b,c]
- 列表推导式:[x for x in iterable]
- 构造器: list(), list(iterable)

### 特点
- 方括号之间`[]`逗号分隔的元素列表.
- 列表截取可以有第三个参数 步长
- 索引可以为正/负，正从0开始，负从-1(tail)开始.

```
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
```

逆序打印:
```
def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]
 
    # 重新组合字符串
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
```

### 操作/方法:
- 截取
- append()
- del 
- 操作符: `+*`
- 函数: `len(list), max(list), min(list), list(seq)`
- 方法: `lsit.append(obj), list.count(obj), list.extend(seq), list.index(obj), list.insert(index, obj)`

## tuple
通常用于储存异构数据的多项集，例如enumerate()内置函数所产生的2元组

### 特点

- 元素不能修改
- 使用逗号分隔元素
- 小括号创建


```
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

# 元组中只包含一个元素时要注意:


```

## range对象
- 不可变的数字序列，通常用在for循环中指定循环次数
- range对象占用固定数量的内存，只保存了start, stop, step.

## str 文本序列类型

```
str = 'Runoob'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串
```

- 使用`r`来raw string: `print(r'Ru\noob'')`
- 单引号与双引号 具有同样的效果
- `*` 多次输出, `+` 连接

### 常识
- 字符串运算符: `+*[] in not in r/R %`
- 字符串格式化: %
- 辅助格式化: `str.format()`, 格式化符号:`*-, +, <sp>, 0, m.n`
- 三个引号: 多行字符串. 常用于html, SQL块
- python 3.6中引入了f字符串，类似于JS中的字符串模板.

### 字符串序列方法
- `str.format()`
- `str.index(sub[, start[, end]])`
- `str.isalnum(), str.isalpha(), str.isascii(), str.isdecimal(), str.isdigital(), str.isidentifier()`
- `str.islower()` `str.isnumeric()` `str.isprintable()` `str.isspace()` `str.istitle()`

## 二进制序列类型--- bytes, bytearray, memoryview
`class bytes([source[, encoding[, errors]]])`
bytes:字面值: b''或者
bytes 字面值中只允许 ASCII 字符（无论源代码声明的编码为何）。 任何超出 127 的二进制值必须使用相应的转义序列形式加入 bytes 字面值。
但 bytes 对象的行为实际上更像是不可变的整数序列，序列中的每个值的大小被限制为 0 <= x < 256 (如果违反此限制将引发 ValueError)
其他创建方式:
bytes(10)
### bytes methods
- classmethod formhex(string)
```python
bytes.fromhex('2Ef0 F1f2  ') #忽略空格
#b'.\xf0\xf1\xf2'
```
- hex([sep[, bytes_per_sep]])
```python
b'\xf0\xf1\xf2'.hex()
#'f0f1f2'
value = b'\xf0\xf1\xf2'
value.hex('-')
#'f0-f1-f2'
value.hex('_', 2)
#'f0_f1f2'
b'UUDDLRLRAB'.hex(' ', -4)
#'55554444 4c524c52 4142'
```

### bytearray对象
bytearray对象是bytes对象的可变对应物
没有专属的


## set
- 使用大括号,或者set()函数
- 无序，唯一, 无固定位置
- 不支持索引，切片

创建
1. 字面量逗号分隔大括号`{value, value2, ...}`
2. 集合推导式: `{c for c in 'abracadabra' if c not in 'abc'}`
3. 使用类型构造器: `set(),   set('foobar')` 

操作:
1. 集合类操作
2. 元素操作: add(elem), remove(elem)

examples:
```python
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
```

## Dictionary
calss dict(**kwargs)
class dict(mapping, **kwargs)
class dict(iterable, **kwargs)

创建：
1. key:value 逗号分隔，
2. 字典推导式: `{x: x ** 2 for x in range(10)}`
3. 类型构造器: `dict()`, `dict([('foo',100), ('bar', 200)])`



```
#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
```

构造函数:dict(d)
d可以是元素的列表，集合，或者元组.
```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f
#True
```

### 字典视图对象
dict.key(), dict.values(), dict.items()

### 类型转换
- int(x)
- float(x)
- complex(real, [,img])
- str(x)
- repr(x)
- eval(x)
- tuple(s)
- lsit(s)
- set(s)
- fronzenset(s)
- chr(x)
- ord(x)
- hex(x)
- oct(x)

## 推导式子
一种独特的数据处理方式，从一个序列构建另一个新的数据序列.
- list推导式
- dict推导式
- set推导式
- tuple推导式

### 列表推导式
```
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_lsit]

或者
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
[结果值1 if 判断条件 else 结果2  for 变量名 in 原列表]


# exmaple
>>> names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
>>> new_names = [name.upper()for name in names if len(name)>3]
>>> print(new_names)
['ALICE', 'JERRY', 'WENDY', 'SMITH']

>>> multiples = [i for i in range(30) if i % 3 == 0]
>>> print(multiples)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)
```

### 字典推导式
`{key_expr: value_expr for value in collection}`
或者
`{key_expr: value_expr for value in collection if condition}`
example:
```
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
>>> newdict = {key:len(key) for key in listdemo}
>>> newdictx
{'Google': 6, 'Runoob': 6, 'Taobao': 6}
>>> dic = {x: x**2 for x in (2, 4, 6)}
>>> dic
{2: 4, 4: 16, 6: 36}
>>> type(dic)
<class 'dict'>
```

### 集合推导式
`{expression for item in Sequence}`
or
`{expression for item in Sequence if conditional}`

```
>>> setnew = {i**2 for i in (1,2,3)}
>>> setnew
{1, 4, 9}

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> type(a)
<class 'set'>
```

### tuple推导式
`(expression for item in Sequence)`
or
`(expression for item in Sequence if conditional)`
可以利用range区间，tuple, list, dict, set等数据类型，快速生一个满足制定需求的tuple.


## bytes, bytearray, memoryview
1. bytes 单个字节构成的不可变序列. 由于许多主要二进制协议都基于ASCII文本编码.
2. 字面值只允许0-127, 超过需要使用对应的转义序列

### 创建bytes
1. 字面量(b前缀)
  - 单引号b' '
  - 双引号b" "
  - 三重引号
2. 指定长度的零值填充: bytes(10)
3. 整数组成的可迭代对象: bytes(range(20))

## 运算符
- 成员运算符 in , not in
- 身份运算符 is , id()

in, not in用来测试是否在制定序列中.

## Number
### 数学函数: math.
- abs(x)
- ceil(x)
...

### 随机数函数
- choice(seq)
### 三角函数

### 数学常量


### 内建函数
- 


## python 解释器内置函数
- abs
- aiter(async_iterable,/)和anext()
aiter没有两个参数的版本
- iter(object, /)
- iter(object, sentinel, /)

```python
import asyncio
async def numbers(nums):
    for i in range(nums):
        yield i
        await asyncio.sleep(0.5)
# 隐式使用
[i async for i in numbers(10) if i % 2 == 0]
# 显式使用
[i async for i in aiter(numbers(10)) if i % 2 == 0]
# [0, 2, 4, 6, 8]
a = aiter(numbers(10))
dir(a)
```

- any(iterable,/)
- bin(x, /), bool(x=Flase/)
- bool(x = False, /)
- breakpoint(*args, **kws)
- class bytearray(): bytes数组,可变序列; class bytes():bytes对象，不可变序列.
- callable()
- chr(i, /), ord()的逆函数
- @classmethod: 把一个方法封装成类方法, 函数的decorator
- class complex(real=0, imag=0), class complex(string, /): 注意字符串转换时+_不能有空格
- delattr(object, name, /) setattr()
- class dict(**kwarg), class dict(mapping, /, **kwarg), class dict(iterable, /, **kwarg)
- dir(), dir(object, /)
- divmod(a, b, /), 等效于(a//b, a%b)
- enumerate(iterable, start = 0)
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# 等价于:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

```

- eval(expression, /, globals=None, locals=None)
- exec(object, /, globals=None, locals=None, /, *, closure=None)

- filter(function, iterable, /) 相当于: (item for item in iterable if function(item)) 生成器表达式
```python
list(filter(lambda n: n > 2, list(range(5))))
>>> numbers = [-2, -1, 0, 1, 2]

>>> # Using a lambda function
>>> positive_numbers = filter(lambda n: n > 0, numbers)
>>> positive_numbers
<filter object at 0x7f3632683610>
>>> list(positive_numbers)
[1, 2]

>>> # Using a user-defined function
>>> def is_positive(n):
...     return n > 0
...
>>> list(filter(is_positive, numbers))
[1, 2]

```

- class float(x=0.0, /)
```python
float('+1.23')
1.23
float('   -12345\n')
-12345.0
float('1e-003')
0.001
float('+1E6')
1000000.0
float('-Infinity')
-inf
```
- frozenset(iterable=set(), /)
- globals()
- hasattr(object, name, /)
- hash(object, /)
- help()
- hex(x, /), oct(x, /)
- input()
- input(prompt, /)
- class int(x, /, base=10)
- len
- class list(iterable, /)

- map(function, iterable, /, * iterables)

- max(iterable, /, *, key=None) , min

- open(file, mode='r',)
-print(*objects, sep=' ', end=)
- slice(stop, /), slice(start, stop, step=1, /): 返回slice对象.
- sorted(iterable, /, *, key=Node, reverse=False), key比较函数.
- sum(iterable, /, start=0) 
- super(type, object_or_type=Node, /)
- tuple
- tuple(iterable, /)
- vars()


- zip(*iterables, strict=False)
zip:返回元组的迭代器
```python
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

(1, 'sugar')
(2, 'spice')
(3, 'everything nice')
```

## 内置常量
- False, True, Non, NotImplemented, Ellipsis, 
- __debug__