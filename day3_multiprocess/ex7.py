from multiprocessing.dummy import Pool
import time
import os

def talk(msg):
    print('msg:',msg)
    time.sleep(3)
    print('end')

if __name__ == "__main__":
    print('开始执行程序：')
    start_time = time.time()
    pool = Pool(3)
    print('开始执行三个子进程')
    for i in range(3):
        #pool.apply(talk,[i])
        pool.apply_async(talk,[i])
    pool.close()
    pool.join()
    print('id号：%s主进程结束 总耗时：%s' %(os.getpid(),time.time()-start_time))
