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

## socket
- socket: Berkely socket api: 低级别网络api.
- socketserver: 高级别网络服务模块

### BSD socket api:
1. 创建coket. 
`int socket (int family, int type, int protocol);`
    - family: AF_INET: IPV4(32bit)+16bit port.
    - type: socket类型: SOCK_STREAM, SOCK_DGRAM
- bind(): 用在服务器侧,和一个套接字地址结构相连，比如说是一个特定的本地端口号或者IP
- listen():  服务器侧
- connect(): client侧
- accept() 服务器侧，从client接受请求创建一个新的tcp连接，并把一个套接字和这个连接相联系
- send()/recv(), write()/read(), sendto()/recevfrom
- close()

#### 用法:
- 服务器: socket(), bind(), listen(), accept()(多个客户端则可以重复执行accept()),对于sendall()_/recv(),使用在connect()返回的套接字上发送.
- 客户端执行: socket(), connect(),在套接字对象上recv,sendall()

### TCP

#### TCP flags
- SYN
- ACK
- FIN: close a connection
- RST- Aborts a connection in response to an error.
- PSH:
    - 应用程序通知TCP立即发送-buffer. PSH flag通知接收host数据立即推送到接收应用程序
    
