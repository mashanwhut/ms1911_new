'''
进程池练习
'''
from multiprocessing import *
import time

#进程池事件
def worker(msg):
    time.sleep(2)
    print(time.ctime(),'--------',msg)

#创建进程池
pool = Pool(10)

for i in range(10):
    msg = 'Tedu %d'%i
    pool.apply_async(func=worker,args=(msg,)) #维持执行的进程总数为processes(Pool指定的进程个数)，当一个进程执行完毕后会添加新的进程进去
    #apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，直接进入下面的代码执行，apply(func[, args[, kwds]])是阻塞的，所有进程执行本行完成后才执行下面的代码
#time.sleep(2)
pool.close() #关闭进程池，就不能在使用apply_async执行新的事件了,使其不在接受新的任务。
pool.join() #回收进程池,主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。

