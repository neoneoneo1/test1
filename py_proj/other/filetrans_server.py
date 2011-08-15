"""
Программа принимает по сети и сохраняет на диск C:\recv 10 файлов 1.jpg...10.jpg
принимает сначала строку инициализации и по принятому размеру файла высчитывает 
количество ожидаемых кусков, столько раз и принимает в ожидающем recv
Многопоточная, по потоку на соединение
1 соединение = 1 файл
"""
#винсок
import socket
import sys
import os
import random
import threading
import time


#Локальный узел
HOST='localhost'
PORT=1000

def getFilSize(initstr):
    s=string.split(initstr,'!')
    s=string.split(str(s[1]),'\'')
    return int(s[1])

def getFilName(initstr):
    s=string.split(initstr,'!')
    s=string.split(str(s[2]),'\'')    
    return str(s[1])

def getFilId(initstr):
    s=string.split(initstr,'!')
    s=string.split(str(s[3]),'\'')    
    return str(s[1])


#Функция потока
def recvThr(str1,addr,conn):
    #print str1
    rnd=int(random.random()*10)
    print 'Подсоединились с адреса:', addr,',ждать секунд:',rnd    
    time.sleep(rnd)
    print "поток с адреса "+str(addr)+" завершен "
    initstr=string.rstrip(conn.recv(1024))
    #Получение заголовка со служебной инфой
    fil_size=getFilSize(initstr)
    fil_name=getFilName(initstr)
    fil_id=getFilId(initstr)
    #print fil_name,fil_size,fil_id
    frames_count=int(fil_size/1024)
    if not (frames_count*1024) == fil_size:
        frames_count+=1
    print fil_name,'frames_count='+str(frames_count)
    
    fil=open('c:/recv/'+fil_name,'wb')
    for i in xrange(frames_count):
        bytes=conn.recv(1024)
        fil.write(bytes)
    fil.close()
    conn.close()
    print 'Файл принят\n'
    #Запись полученных кусков в файл


#Сервер
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)


while 1:
    conn,addr=s.accept()
    my_id_thr="Thr1"    
    pThr = threading.Thread(target=recvThr, name=my_id_thr, args=[my_id_thr,addr,conn]) 
    pThr.start()



#на будущее
#>>> from subprocess import *
#>>> command_stdout = Popen(['ls', '-l'], stdout=PIPE).communicate()[0]
"""