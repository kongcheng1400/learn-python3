## 数据及变量
### 基本类型
数字: int, float, complex

#### 运算
- 逻辑值检测:if, while
- 布尔运算: and, or, not, not优先级比非布尔运算符低
- 比较运算: 八种比较，优先级相同，可以串连: < <= > >= == != is is not

### 复合类型
基本序列类型: list, tuple, range
附加序列类型: str, 二进制序列类型bytes, bytearray, memoryview
集合: set, frozenset
映射: dict
不可变序列类型 VS 可变序列类型: 区别在于hash()内置函数的支持.
#### 创建复合类型
字面量: list 方括号，tuple 圆括号
列表推导式: l=[i for i in range(5)]
构造函数模式: list(range(5)), list(iterable),

#### 通用序列操作
- x in s
- x not in s
- s + t, s * n, n * s
- s[i]
- s[i:j]
- len(s), min(s), max(s)
- s.index(x,[, i[, j]])
- s.count(x)

#### 可变序列类型的运算
- s[i] = x
- s[i:j] = t
- del s[i:j]
- s.append(x)
- s.clear() 等同于del s[:]
- s.copy() 等同于s[:]
- s.extend(t) 或 s += t
- s *= n
- s.insert(i, x) == s[i:i] =[x]
- s.pop() , s.pop(i)
- s.remove(x)
- s.reverse

## 文本序列/文本处理服务/string模块
- class str(object='')
- class str(object=b'', )
### 常量部分
主要是各种字符。略去.
### 格式化
- str.format()方法, 格式字符串语法.
- 模板字符串:基于$的替换.
- f-string
- printf风格的字符串.
### 辅助方法
- str.captialize()
- str.casefold() vs lower()
- str.count(sub, start, end)
- str.encode()
- str.endswith(suffix, start, end)
- str.expandtabs(tabsize=8)
- str.find
- str.format
- str.format_map(mapping)
- str.index 
- str.sialnum, isalpha, isacsii, isdecimal, isdigit, isidentifier, islower, is numeric, ispritable, isspace, ittitle, is upper
- str.join(iterable)
- str.ljust(width, ), lstrip, 
- str.lower, 
- str.partition(sep)
- str.removeprefix, removesuffix, replace, find, rindex, rsplit, rstrip, splitlines, swapcase, title

## 二进制序列类型 bytes, bytearray, memoryview
- bytes: ASCII金融数据的处理.
- bytearray: 可变bytes.
- 支持缓冲区协议

### 缓冲区协议

## 其他类型
- GenericAlias, Union

## 内置函数
- ord(), chr(), ord('a')
## exception
BaseException
Exception
- try的else子句:在未触发异常时执行。
## 流程控制
while, if-elif-else, 
for xx in xxx
range/enumerate
循环语句中的else子句: for中循环完成之后，执行else子句. while 条件为假时，执行.
### match-case:
通配符适配: case _:, 组合多个字面值: case 401 | 402 | 404:
模式的形式类似解包赋值，并可用于绑定变量:


## 函数
- 函数局部变量符号表.
- 实参引入到被调用函数的局部符号表.
- 函数返回值. 没有return返回None. 
- 位置参数, 默认值参数, 关键字参数.
- 特殊参数. / *
- 解包实参列表: *, **

### lambda表达式


## OOP

## 标准库
- struct()

## 编码风格
- PEP-008
### 书写风格
- 一行/两行空格 顶级函数/类 两行
- 长算式运算符一起换行


## Data structure and algorithm

### 基本操作
- 访问/查找元素
- push/pop
- insert, del