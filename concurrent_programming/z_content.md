#### 并发编程

##### 1. 程序运行的底层原理

<img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120100357869.png" alt="image-20221120100357869" style="zoom:40%;" />

* 进程： 将程序加载到内存中（指令和数据）, 资源分配的基本单位
* 线程：程序执行的基本单位
* 程序如何运行：cpu读指令 - > pc (存储指令地址) -> 读取数据 register -> 计算， 回写，下一条指令
  * 寄存器： register ( 存数据用的)
  * pc：程序计数器
  * ALU：计算单元
  * eg： 一个线程要计算 2 + 3 ;  将2，3 放入到寄存器、将计算结果写回内存、pc指向下条指令
* **线程如何进行调度：**线程调度器，（os）操作系统
* **线程切换的概念：**context switch cpu 保存线程，执行新的线程 ->恢复现场, 继续执行原线程

##### 2. python并发编程

* 并发编程引入： 程序提速

* 程序提速方法有哪些：

  <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120103244229.png" alt="image-20221120103244229" style="zoom:50%;" />

* Python对并发编程的支持

  * 多线程：threading , 利用cpu和io可以同时执行的原理，让cpu不会一直等待io完成
  * 多进程：multiprocessing， 利用多核cpu的能力，真正并行任务
  * 异步io：asyncio, 在单线程利用cpu和io同时执行，实行函数的异步执行

* python 提供的辅助功能

  * 使用lock对资源加锁，防止冲突和访问
  * 使用Queue实现不同线程/ 进程之间的数据通信，实现生产者、消费者模式
  * 使用线程池Pool / 进程池 Pool , 简化线程/进程的任务提交、等待结束、获取结果
  * 使用subprocess 启动外部程序的进程，并执行外部输入输出的交互

* python 三种编程方式的选择

  * 多进程 Process （一个进程可以开启n个线程）
    * 优点：可以利用多核cpu并行运算
    * 缺点：占用资源最多，可启动数目比线程少
    * 适用于：cpu密集型计算
  * 多线程Thread（一个线程可以启动N个协程）
    * 优点：相比进程更加轻量级，占用资源少
    * 缺点：相比进程， 多线程只能并发执行，不能利用多cpu（GIL）,相比协程，启动数目有限制，占用内存资源，有线程的切换的开销
    * 适用于：IO密集型的计算，同时运行的任务数目要求不多
  * 多协程coroutine
    * 优点：内存开销最少，启动协程的数量最多
    * 缺点：支持的库有限制，代码较为复杂

##### 3. python慢的原因

* 动态类型的语言， 边解释边执行
* GIL （全局解释器锁）
  * 是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行
  * 即便在多核处理器上，使用GIL的解释器也只允许同一时间执行一个线程
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120113050041.png" alt="image-20221120113050041" style="zoom:40%;" />
  * 相比并发加速的c++， java (如果开启了多线程，多线程会分布到多核上同时执行)
  * 为什么会有GIL,  在设计之初为了解决多线程之间数据完整性和状态同步的问题
    * python中的对象管理使用的是引用计数，引用计数为0则释放对象
    * 如果不加锁会导致引用计数的混乱
    * 简化了python对共享资源的管理
  * 怎样规避GIL带来的限制
    * 用于io密集性计算
    * multiprocessing多进程机制实现并行计算，利用多核cpu应对

##### 4. python 线程安全

* 线程安全：线程安全是指某个函数、函数库在多线程环境中被调用时候，能狗正确的处理多个线程之间的共享变量，使程序能够正确完成
* 由于线程只想随时会发生切换，就操成了不可预料的结果，出现线程不安全

##### 5. python 线程池

* 线程池的原理
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120165850713.png" alt="image-20221120165850713" style="zoom:30%;" />
* 使用线程池的好处
  * 提升性能： 因为减去了大量的新建，终止线程的开销，重用了线程资源
  * 适用场景：适合处理突发性的大量请求或需要大量线程完成的任务、但是实际任务处理较短
  * 防御功能：能有效的避免系统因为创建线程过多，而导致系统负荷过大相应变慢等问题
  * 使用线程池的语法比自己新建线程执行线程更加简洁
* Thread PoolExecutor 使用的语法
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120170443117.png" alt="image-20221120170443117" style="zoom:50%;" />

##### 6. python 线程池

* 有了多线程threading，为什么还要用多进程multiprocessing
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120183415834.png" alt="image-20221120183415834" style="zoom:50%;"/>
  * nultiproessing模块就是python为了解决GIL缺陷引入的一个模块，原理是用多进程在cpu上并行执行
* 多进程的知识梳理：
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120183742592.png" alt="image-20221120183742592" style="zoom:40%;" />

##### 7. python 线程池在web服务中的应用

* web 服务的架构的特点
  * <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120181048372.png" style="zoom:50%;" />
* 使用线程池ThreadPoolExecutor加速
  * 方便的将磁盘文件、数据库、远程API的IO调用并发执行
  * 线程池的线程数目不会无限的创建（导致系统挂掉），具有防御功能

##### 8. 异步io asyncio

* <img src="/Users/wangcx/Library/Application Support/typora-user-images/image-20221120183928791.png" alt="image-20221120183928791" style="zoom:40%;" />