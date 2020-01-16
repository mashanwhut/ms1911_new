'''
multiprocessing练习
'''
import multiprocessing
import time,os

a = 1

def fun():
    print('2020第一个代码',time.time())
    time.sleep(3)
    global a
    a = 1000
    print(time.time())

#1、只创建子进程
p = multiprocessing.Process(target=fun) #创建进程对象
p.start() #启动进程
p.join() #回收进程,父进程会阻塞等待子进程执行完成
print(time.time())

#2、同上的原理
'''
pid = os.fork()
if pid == 0:
    fun()
    os._exit(0)
else:
    os.wait()
'''
#3、父进程也同时执行事件
p = multiprocessing.Process(target=fun) #创建进程对象
p.start() #启动进程
print('父进程执行开始：',time.time())
time.sleep(2)
print('父进程执行结束：',time.time())
p.join() #回收进程,父进程会阻塞等待子进程执行完成
print(time.time())
print(a) #父进程不受子进程影响



