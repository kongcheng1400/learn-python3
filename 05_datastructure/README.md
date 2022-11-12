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