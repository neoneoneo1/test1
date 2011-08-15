"""
Программа открывает на диске C 10 файлов  1.jpg...10.jpg
отсылает серверу строку инициализации с именем, размером и идентификатором
передает их на сервер кусочками по 1024 байта в разных потоках
по потоку на соединение
"""
#винсок
import socket
import sys
import os
import random
import threading
import time
import string


#Клиент читает фотку рубит кусочками и шлет



"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
rez=1
HOST='localhost'
retry=0
fil_name='1.jpg'
fil_size=os.path.getsize('c:/'+fil_name)
fil_id=int(random.random()*100000)
print '<file !fil_size=\''+str(fil_size)+'!fil_name=\''+str(fil_name)+'!fil_id=\''+str(fil_id)+'!></file>'
dic={'file':fil_id,'fil_size':fil_size,'fil_name':fil_name}
print str(dic)
"""

"""
while not rez=0:
    PORT=int(random.random()*65511)
    rez=s.connect_ex((HOST,PORT))
    retry+=1
    if retry==65511: #65 тыс попыток сменить порт
        break
if rez==0:
    s.send('<file size='fil_size'></file>')
    data=s.recv(1024)
    print 'Полученные данные:',data
else:
    print 'Не удалось соединиться с сервером'
s.close()
"""

"""
#Рабочее чтение файла кусками
rez=1
HOST='localhost'
retry=0
fil_name='1.jpg'
fil_size=os.path.getsize('c:/'+fil_name)
fil_id=int(random.random()*100000)
#print '<file !fil_size=\''+str(fil_size)+'!fil_name=\''+str(fil_name)+'!fil_id=\''+str(fil_id)+'!></file>'
#Первая посылка общие данные, дальше идентификатор файла и данные
dic={'file':fil_id,'fil_size':fil_size,'fil_name':fil_name}
bytes=str(dic).ljust(1024)
#print bytes

fil=open('c:/1.jpg','rb')
fil1=open('c:/1.jpg','wb')
#Послать сообщение о начале передачи файла с заданным идентификатором
while 1:
    bytes=fil.read(1024)
    if bytes:
        #Тут дополнить кусок до 1024
        if len(bytes)<1024:
            bytes=bytes.rjust(1024)
            #print len(bytes)
        #тут слать кусок по сети
        fil1.write(bytes)
    else:
        break
fil.close()
fil1.close()
"""



    
"""
HOST='localhost'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
rez=s.connect_ex((HOST,PORT))
data=''
if rez==0:
    s.send('from client to serv')
    data=s.recv(1024)
    print 'Полученные данные:',data
else:
    print 'Не удалось соединиться с сервером'
s.close()

        #Инициализация сокета
    #while count<5:
    #пока читается файл
        #Чтение кусочка из файла
    #    cond.acquire() 
        #var1[0][0]=int(random.random()*10)
        #Отсылка данных в сокет
    #    cond.notifyAll()
    #    cond.release()


def sendThr(str1,cond,*var1):
    print str1

var1=[]
cond=threading.Condition()
t1 = threading.Thread(target=sendThr, name="t1", args=["Thread No:1",cond,var1])
t2 = threading.Thread(target=sendThr, name="t2", args=["Thread No:2",cond,var1])
t1.start()
t2.start()
"""



class Upload:
    #Конструктор
    def __init__(self,to_host='localhost',to_port=1000):
        #self.from_host=from_host
        #self.from_port=from_port
        self.to_host=to_host
        self.to_port=to_port
        self.progress=0
        self.bConnected=False
        #Инициализация сокета
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        rez=self.s.connect_ex((self.to_host,self.to_port))
        if rez==0:
            self.bConnected=True
        else:
            print 'Не удалось соединиться с сервером'
        #Создание потока
        var1=[0,threading.Condition()]
        my_id_thr='Thr'+str(int(random.random()*10))
        self.pThr = threading.Thread(target=self.sendThr, name=my_id_thr, args=[my_id_thr,var1])

        
    
    #Деструктор
    def __del__(self):
        self.s.close()
        print "деструктор"

    #Запуск начала закачки
    def startDownload(self,file_name_full):
        #Запуск потока
        self.file_name_full=file_name_full
        self.file_basename=os.path.basename(file_name_full)
        self.pThr.start()
        

    #Функция потока
    def sendThr(self,str1,*var1):
        #print str1
        #print var1
        #Если есть соединение        
        if self.bConnected:
            #Пока читается файл, кусками засылать его
            #Пока что готовить пакеты с нулями и слать
            #Представление пакета файла
            fil_size=os.path.getsize(self.file_name_full)
            fil_id=int(random.random()*100000)
            initstr='<file !fil_size=\''+str(fil_size)+'!fil_name=\''+str(self.file_basename)+'!fil_id=\''+str(fil_id)+'!></file>'
            initstr=initstr.rjust(1024)            
            self.s.send(initstr)
            #Открыть файл и начать чтение кусков и передачу этих кусков
            fil=open(self.file_name_full,'rb')
            bytes_sent=0
            while 1:
                bytes=fil.read(1024)
                if bytes:
                    #Тут дополнить кусок до 1024
                    bytes_sent+=1024
                    if len(bytes)<1024:
                        bytes=bytes.rjust(1024)
                        bytes_sent+=len(bytes)
                    #тут слать кусок по сети
                    self.s.send(bytes)
                    if bytes_sent>0:
                        self.progress+=int(fil_size/(bytes_sent*100))
                else:
                    break
            fil.close()
            self.progress=100
        #time.sleep(1)




files_count=10

#Заполнение списка закачек
dw_list=[]
for i in xrange(files_count):
    dw_list.append(Upload('localhost',1000))
    fullp='c:/'+str(i+1)+'.jpg'
    dw_list[i].startDownload(fullp)

#Поток мониторящий список закачек
def monitor_Dw(dw_list):
    bEnd=False
    while not bEnd:
        bEnd=True
        print '\n=============='
        for i in xrange(len(dw_list)):            
            if dw_list[i].progress<100 and dw_list[i].bConnected:
                bEnd=False
            if dw_list[i].progress<=100 and dw_list[i].bConnected:
                print str('file:'+dw_list[i].file_name_full).ljust(30)+str(dw_list[i].progress)+'%'
        print '==============\n'
        time.sleep(0.5)
    
monitor_Dw(dw_list)

#Подчистка списка с конца
for i in xrange(files_count):
    del dw_list[files_count-1-i]
print 'Конец передачи'

#initstr='<file !fil_size=\''+str(100)+'!fil_name=\''+str('1.jpg')+'!fil_id=\''+str('0123456789')+'!></file>'
