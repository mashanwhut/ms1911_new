'''
消息队列：双色球
'''
import multiprocessing
from multiprocessing import *
from random import randint
import os,shutil,tqdm,time

#创建消息队列
q = Queue(10)
def handle():
    while True:
        x = randint(1,33)
        q.put(x) #放入消息队列

def recv():
    l = []
    while len(l)<6:
        x = q.get()
        if x not in l:
            l.append(x)
    l.sort()
    l.append(randint(1,16))
    print(l)

p1 = Process(target = handle)
p2 = Process(target = recv)
p1.daemon = True #父进程结束p1进程也随之结束，在start()之前设置
p1.start()
p2.start()

p2.join()

'''
练习3：使用进程池拷贝一个目录（包含目录中所有内容），目录中包含若干个普通文件。
要求：
1、目录中的每个文件拷贝过程都需要一个单独的进程去完成
2、拷贝过程中实时显示拷贝的百分比

'''
src_dir = '/home/tarena/PycharmProjects/month2/week2/day1_http/'
des_dir = '/home/tarena/PycharmProjects/month2/week2/backup/'

def copy_file(src_file, des_file):
    f_r = open(src_file,'rb')
    f_w = open(des_file,'wb')
    while True:
        data = f_r.read(1024)
        if not data:
            break
        n = f_w.write(data) #返回值是本次写入的字节数
        q.put(n)
    f_r.close()
    f_w.close()

files = os.listdir(src_dir)
total_size = sum([os.path.getsize(src_dir+file) for file in files])
# print(files) #只有文件名，不是绝对路径
if os.path.exists(des_dir):
    shutil.rmtree(des_dir)
os.mkdir(des_dir)

q = Queue()
pool = Pool()
for file in files:
    src_file_path = src_dir + file
    des_file_path = des_dir + file
    pool.apply_async(func=copy_file, args=(src_file_path,des_file_path))
pool.close()

copy_size = 0
while True:
    #time.sleep(0.01)
    print(q.qsize())
    copy_size += q.get()
    print('=====进度====%f%%===='%(copy_size * 100/total_size))
    if copy_size >= total_size:
        break
pool.join()








