# 基本数据类型
不可变: Number(int, float, complex,bool), String, Tuple
可变: List, Dictionary,Set

- 数字类型是不允许改变的，改变之后重新分配存储空间，可以使用del删除引用。

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

## string

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

## 序列
- 6个内置的序列类型，最常见的是列表和元组.

## List
- 序列是python中最基本的数据结构

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

### set
- 使用大括号,或者set()函数
- 无序，唯一.

创建
```
parame = {value01,value02,...}
或者
set(value)

```

examples:
```
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

### Dictionary
使用{}创建的key:value pair
或者使用dict()
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
```
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
```

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

## String
### 常识
- 使用[]来截取字符串.
- 字符串运算符: `+*[] in not in r/R %`
- 字符串格式化: %
- 辅助格式化: `str.format()`, 格式化符号:`*-, +, <sp>, 0, m.n`
- 三个引号: 多行字符串. 常用于html, SQL块
- python 3.6中引入了f字符串，类似于JS中的字符串模板.

### 内建函数
- 


