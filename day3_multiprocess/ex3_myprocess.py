'''
重定义Process类
'''
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,value):
        super().__init__()
        self.value = value
    def fun1(self):
        time.sleep(2)
        print('步骤1')
    def fun2(self):
        time.sleep(2)
        print('步骤2')
    def run(self):
        self.fun1()
        self.fun2()

if __name__ == '__main__':
    p = MyProcess(2)
    p.start() #自动执行run()
    p.join()