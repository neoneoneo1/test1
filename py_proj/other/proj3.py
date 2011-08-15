import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

i=1
def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        print i
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    #i+=2
    with cond:
        logging.debug('Making resource available')
        print i
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

# import threading
# import time
# #Пример: через переопределение класса threading.Thread
# #Поток выполняется пока работает run()
# #Один поток
# cond=threading.Condition()
# bStop=0
# var1=0
# def thred_fun1():
#     while  bStop<1:
#         if var1==0:
#             cond.acquire() #Заблокировать поток другим ждать
#             time.sleep(1)        
#             var1='Из пишущего потока'
#             print var1
#             cond.notify()#Предупредить других что разблокировал
#             cond.release()#разблокировать
# def thred_fun2():
#     while  bStop<1:
#         cond.acquire() #Заблокировать поток другим ждать
#         #while var1==0:
#         cond.wait()
#         print 'from thread2 var1=',var1
#         time.sleep(1)
#         cond.release()#разблокировать
#         if var1==1:
#             var1=0
#         
# thr1=threading.Thread(None,thred_fun1,"MyThread1")
# thr2=threading.Thread(None,thred_fun2,"MyThread2")
# 
# 
# 
# thr1.start()
# thr2.start()
# time.sleep(10)
# bStop=1
# 
# 
# 
# #Подождать пока поток сдохнет
# while thr1.isAlive() and thr2.isAlive():
#     pass
#     
# time.sleep(1)
# """
# if thr1.isAlive():
#     print 'thr1.isAlive\n'
# else:
#     print 'dead1\n'
#     
# if thr2.isAlive():
#     print 'thr2.isAlive\n'
# else:
#     print 'dead2\n'
# """
# 
# print "\nэт конец"

# a=[1]
# def ff(par):
#     par[0]=2
# 
# print a[0]
# ff(a)
# print a[0]