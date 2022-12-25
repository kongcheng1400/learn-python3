
## control


### while

```
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```


```
end 关键字:
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

```

### if
```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

```

### match...case
```python
match subject:
    case <pattern_1>:
        <action_1>
    #case 可以使用隔开: |
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

### loop

#### while

```python
while condition:
    statement(s)...
```

or `while else`
```python
while expr:
    <statement(s)>
else:
    <additional_statement(s)>
```

简单与剧组:
只有一条可以写同一行:类似if
`while (flag): print('welcome!')`

#### for 
迭代完成的时候执行else.
```python
for <varaible> in <sequence>:
    <statements>
else:
    <statements>
```

#### range()函数
生成序列:其他集合可用此序列构造集合.
enumerate: enumerate(iterable, start=0): 返回一个枚举对象，其迭代器的__next__()方法返回一个元组，里面包含一个计数值()
- range(stop)
- range(start, stop)
- range(start,stop, step)
_ 

```python
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

#### pass
pass是空语句，保持结构的完整性:
```python
while True:
    pass
```

## 迭代器与生成器与容器

### iterable:可迭代对象.
iterable:可迭代对象: 所有的序列类型: list, str, tuple, 和一部分非序列类型:dict, file objects, 和所有定义了__iter__(), __getitem()___方法的class. 实现了sequence 语义。

- 内置函数iter(iterable)可以返回迭代器.
- 可迭代对象可被用于for循环以及许多其他需要一个序列地方(zip(), map()), 不要自己处理迭代器对象，for会为你自动处理.
### 迭代器iterator/迭代器协议
1. 两个内置函数 `iter()`, `next()`, 或者迭代器的`__next__()`方法, `__iter__()`方法
2. 迭代器协议: 迭代器对象本身需要支持:`__next__()`方法, `__iter__()`方法

```python
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

```

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
### 生成器generator
```
yield_atom       ::=  "(" yield_expression ")"
yield_expression ::=  "yield" [expression_list | "from" expression]
```
1. 生成器提供了实现迭代器协议的便捷方式:如果容器对象的__iter__()方法被实现为生成器，它将自动返回一个迭代器对象
2. 写法就像写函数. 每次在生成器上调用next()时，会从上次离开的位置恢复执行.
yield表达式只有在定义generator函数或者aynschronous generator函数时才会用到，因此只能在函数定义的内部使用.

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
```

## 输入和输出
- 表达式语句
- 内置print()函数,f string, str.format(), printf风格
- 内建format(value, 'format_spec')函数.
  - `str()` 用户易读
  - `rstr()` 解释器易读的表达形式

### 格式化
两种: 一种是str.format()和自定义字符串格式化， 一种是基于C printf样式的格式化

#### str.format(*args, **kwargs)


```
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | digit+]
attribute_name    ::=  identifier
element_index     ::=  digit+ | index_string
index_string      ::=  <any source character except "]"> +
conversion        ::=  "r" | "s" | "a"
format_spec       ::=  <described in the next section>
```

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # 注意前一行 'end' 的使用
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27

```

str.format: 较新的函数
旧式: `print('常量 PI 的值近似为：%5.3f。' % math.pi)`

### format_spec 格式规格迷你语言
format_spec     ::=  [[fill]align][sign][z][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

### format内置函数

```python
format(14, '#b'), format(14, 'b')
# ('0b1110', '1110')
# fstring
f'{14:#b}', f'{14:b}'
# ('0b1110', '1110')
format(14, '#010x')
#'0x0000000e'
format(14, '#010_x')
#'0x000_000e'
format(14, '#10x')
#'       0xe'
format(3.123344E+1, '#5.2f')
#'31.23'


"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
#'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
'{:,}'.format(1234567890)
#'1,234,567,890'
'{:_}'.format(1234567890)
#'1_234_567_890'
'Correct answers: {:.2%}'.format(2/3)
#'Correct answers: 66.67%'
```

```python
'%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```

#### f-string. 
```
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | NULL | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
```

#### 旧式风格 printf %操作符
`format % values`: %字符串的格式化或者插值运算符.
values: 如果format只有一个参数，则values可以为一个非元组对象。否则必须为一个元组，或者单独映射对象(例如字典)
```python
print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})
# Python has 002 quote types.
```

## 函数
- tuple形参*arguments
- dict形参: **keywords
- 解包参数: *从列表或者
- /:位置形参, * 位置或者关键字, 关键字
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

### docstring
