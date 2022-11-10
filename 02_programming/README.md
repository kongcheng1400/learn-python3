
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
```python
for <varaible> in <sequence>:
    <statements>
else:
    <statements>
```

#### range()函数
- range(stop)
- range(start, stop)
- range(start,stop, step)
_ 

```python
>>>a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
>>> for i in range(len(a)):
...     print(i, a[i])
```

#### pass
pass是空语句，保持结构的完整性:
```python
while True:
    pass
```

## 迭代器与生成器
迭代器的两个基本方法: `iter()`, `next()`

```python
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

```