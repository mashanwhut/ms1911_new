'''
创建多进程multiprocessing.Process
'''
'''
练习1：
'''
from multiprocessing import Process
import time,os

def fun1():
    time.sleep(2)
    print('吃饭')
    print(os.getppid(),'----------',os.getpid())

def fun2():
    time.sleep(3)
    print('睡觉')
    print(os.getppid(),'----------',os.getpid())

def fun3():
    time.sleep(4)
    print('打豆豆')
    print(os.getppid(),'----------',os.getpid())

print(time.time())
p_list = []
for fun in [fun1,fun2,fun3]:
    p = Process(target=fun)
    p_list.append(p)
    p.start()

#一起回收
for p in p_list:
    p.join()

print(time.time())

'''
练习2：传参
'''
def worker(sec,name):
    for i in range(3):
        time.sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

#p = Process(target=worker,args=(2,'pack'))
#p = Process(target=worker,kwargs={'sec':2,'name':'pack'})
p = Process(target=worker,args=(2,),kwargs={'name':'pack'})
p.start()
p.join()

'''
练习3:拆文件：使用Process按照字节大小同时拆成2个文件
'''

def fun(w_file,offset,copy_size):
    print('----%s--start---'%w_file, time.time())
    f1 = open('bc.jpg', 'rb')
    f2 = open('%s'%w_file, 'wb')
    f1.seek(offset)
    #data = f1.read(copy_size) #这种方法大文件处理不当
    #f2.write(data)
    while True:
        if copy_size <= 1024:
            data = f1.read(1024)
            f2.write(data)
            break
        data = f1.read(1024)
        f2.write(data)
        copy_size -= 1024
    print('----%s--over---'%w_file, time.time())
    f1.close()
    f2.close()

file_size = os.path.getsize('bc.jpg')
slice_file_num = 3
r_size = file_size // slice_file_num
p_list = []
for i in range(slice_file_num):
    w_file_name = 'photo%d.jpg'%i
    offset = i * r_size
    if i == slice_file_num -1:
        r_size = file_size - r_size * i
    #p = Process(target=fun,name = 'fun%d'%i,args=(w_file_name,offset,r_size)) #name的使用
    p = Process(target=fun,args=(w_file_name,offset,r_size))
    p.start()
    print(p.name) #没有定义name时：Process-1 /Process-2 /Process-3  如果定义了name则打印的是name 的值fun0/fun1
    p_list.append(p)

for p in p_list:
    p.join()

print(time.time())













