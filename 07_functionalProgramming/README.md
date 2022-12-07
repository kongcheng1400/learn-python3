#

## 生成器表达式和列表表达式
如果迭代器返回一个无线数据流或者大量的数据，列表推导式就不大好用了。这种情况下生成式表达式会更受青睐。

```python

line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
```