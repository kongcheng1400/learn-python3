# python3 数据结构
- 列表可变，字符串和元组不行.
## 列表
- `list.append(x)`
- `list.extent(L)`
- `list.insert(i, x), a.insert(len(a),x) 相当于a.append(x)`
- `list.remove(x)`
- `list.pop([i])`
- `list.clear()` 相当于 `del a[:]`
- `list.index(x)`
- `list.count(x)`
- `list.sort()`
- `lsit.reverse()`
- `lsit.copy()`

### 堆栈
- append(x) 相当于push()
- pop() 

### 队列
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 列表推导式
从序列创建列表的简单途径.
- for 之后可以再有for或者if子句.
```python
>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]
```

### 生成器表达式
```python
line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
```

```
( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3
             ...
             if condition3
             for exprN in sequenceN
             if conditionN )
```

```python

seq1 = 'abc'
seq2 = (1, 2, 3)
[(x, y) for x in seq1 for y in seq2]  
[('a', 1), ('a', 2), ('a', 3),
 ('b', 1), ('b', 2), ('b', 3),
 ('c', 1), ('c', 2), ('c', 3)]
```

## algos
### 动态规划
O(n^2)
要理解Kadane’s Algorithm，首先要理解什么是动态规划。这里简单介绍一下：动态规划本质是一个“记忆系统”，动态规划会把一个复杂的问题转换成一些列小问题，解决当前小问题之后，状态（结果）会保存下来，用来帮助解决下一个小问题，从而避免重复计算。经典的问题如背包问题，爬楼梯问题等等，这里就不赘述了。



### array/lsit

#### 查找相同元素
1. 暴力查找O(n^2)
2. 排序后查找.O(NLn(n))
3. 使用一个dict.

#### 最长单词
1. 确定每个单词的长度，比较出最长的.
2. 使用re.findall找到所有，然后使用max找到推导出的长度数组，然后便利长度数组.


#### 最大sum的子数组.
1. 暴力循环O(n^2)
2. 使用Kadane algo. 动态规划