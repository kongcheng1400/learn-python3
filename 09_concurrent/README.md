# python
- 函数或者使用类来包装线程对象

常用模块：_thread, threading


_thread:低级别，原始的线程及一个简单的锁.
threading: 除了包含_thread 模块中的所有方法外，还提供
    - threading.currentThread()
    - threading.enumerate()
    - threading.activeCount()

## Thread类
- run()
- start()
- join([time])
- isAlive()
- getName()
- setName()
### 使用方法
Thread类：控制线程的运行.
- 传递一个可调用对象给构造函数/或者在子类重载run()方法.
- 只能重载__init__()和run()方法
- 创建之后调用现成的start()方法.

### daemon线程

## 线程同步-多个线程对某个数据修改.
Thread对象的Lock, Rlock可以实现简单的线程同步.
threading.lock
threading.Rlock

### class threading.RLock:
重入锁: 一旦线程获取了重入锁，同一个线程再次获取它将不阻塞；线程必须在每次获取它时释放一次。
- acquire(blocking=true): blocking=True:如果线程已经拥有锁，则递归+1,立即返回. 如果其他线程拥有锁，则阻塞.
- blocking=Flase,不阻塞.
- release():只有拥有锁的才能调用.

### 方法
- 将操作放在acqure和release之间 .


## 线程优先级队列 Queue
- Python的Queue 模块提供了同步的，线程安全的队列类 .
- 这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步.

Queue模块常用方法
- qsize()
- empty()
- full()
- get([block[,timeout]])
- get_nowait() get(False)
- put(item)
- put_nowait() 相当于put(item,False)
- task_done()
- join() 等到队列为空，再执行别的操作.

## threading.local类

# socketserver
- 简化socket的编写.
- 同步类常用 socketserver.TCPServer, socketserver.UDPServer, 还有两个Unix
- 使用ThreadingMixIn可以支持异步行为(创建单独的线程来处理每个请求)
## 创建服务器
1. 子类化BaseRequestHandler类并重载Handle()方法来处理传入的请求.
2. 实例化某个服务器类，将服务器地址和请求处理句柄类传给它。
  - 可以使用with 语句，再调用服务器对象的handle_request()或server_forever()方法来处理一个或者多个请求.
  - 最后，调用server_close()关闭套接字(如果没用with)

### 预定义的混合类
- socketserver.ThreadingTCPServer.

### socketserver.BaseRequestHandler
- handle() 执行请求提供服务所需的全部操作.
- 有几个可用的实例属性：self.request, self.client_address, self.server, 