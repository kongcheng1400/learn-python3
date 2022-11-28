# 标准库

## os
- os.getcwd()
- os.chdir()
- os.system('mkdir today')
- dir(os)
- help(os)

## shutil
```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
>>> shutil.move('/build/executables', 'installdir')
```

##  

## matplotlib
![plot](plot_struct.png)

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.

```
### 组成部分
- figure,所有的子axes
- axes: titles, figure legends, colorbars(2 Axis objects, title, label):绘图的主要入口
- axis: scale, limits, ticks, ticklabels:对象:Locator(tick位置), Formatter(ticklabel strings)
- artist: 每个可见对象都是Artist(Figure, Axes, Axis, Text, Line2D, collections, Patch), 当图形render的时候，所有的Artists画在画布上。

## numpy
![ndarray的内部结构](ndarray.png)

组成:
- 指向数据的指针
- 数据类型dtype,描述数组中固定大小值得格子
- 一个表示数组形状(shape)的元组，表示各维度大小的元组
- 一个跨度stride元组，前进到当前维度下一个元素需要跨过的字节数

`numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)`