# -*- coding: utf-8 -*-
__author__ = 'admin'
#Файлы
fil=open('c:/config.xml','w')
fil.write("строка в кодировке UTF8")
fil.flush() #Сброс внутреннего буфера на диск прям сейчас
print fil.fileno()
fil.close()

fil=open('c:/config.xml','r')
print fil
part_file=fil.read(10) #Читать файл N символов
print "Позиция в файле в байтах от начала",fil.tell()
allfile=fil.read()#Читать весь файл с текущей позиции
one_line=fil.readline();#Читать 1 строку из файла
#all_rows=fil.readlines(); Вернёт содержимое текстового файла в виде списка строк
print part_file
print allfile

#Переместить курсор в начало
#seek(Позиция в байтах,откуда отсчитывать
#0-от начала, 1-от текущей позиции,2 с конца)
fil.seek(0,0)
print fil.isatty() #Если файло-терминал?
#fil.truncate(10) #Обрезка файла до 10 байт - не работает
fil.close


fil=open('c:/config.xml','wb')
fil.write("строка в кодировке UTF8\nстрока в кодировке UTF8\nстрока в кодировке UTF8\nстрока в кодировке UTF8")
fil.close()

fil=open('c:/config.xml','rb')
print fil
part_file=fil.read(10) #Читать файл N символов
one_line=fil.readline();#Читать 1 строку из файла
#all_rows=fil.readlines(); Вернёт содержимое текстового файла в виде списка строк
print "Позиция в файле в байтах от начала",fil.tell()
allfile=fil.read()#Читать весь файл с текущей позиции
print part_file
print allfile
fil.close


#Модуль pickle
#Для записи и чтения из файлов сложных типов данных
#строк, списков, словарей и т д
import pickle

x=range(1,100)
fil=open('c:/config.xml','wb')
pickle.dump(x,fil)
fil.close()

fil=open('c:/config.xml','rb')
x=pickle.load(fil)
fil.close()
print x


fil=open('c:/config.xml','w')
fil.write("строка в кодировке UTF8")
fil.flush() #Сброс внутреннего буфера на диск прям сейчас
print fil.fileno() #Возвращает целое число - дескриптор файла
s=['строка1','строка2']
fil.writelines(s)#запись последовательности в одну строку в файл
print fil.name #Имя открытого файла
print fil.closed #Файл открыт/закрыт
print fil.mode #Режим открытого файла
print fil.softspace
#Должен ли выводиться пробел перед
#выводом следующего значения
#с помощью инструкции print
fil.close()

"""
#Рабочее чтение файла кусками
buffer1=""
fil=open('c:/1.jpg','rb')
#Послать сообщение о начале передачи файла с заданным идентификатором
while 1:
    bytes=fil.read(1024)
    if bytes:
        #Тут дополнить кусок до 1024
        if len(bytes)<1024:
            bytes=bytes.rjust(1024)
            print len(bytes)
        #тут слать кусок по сети
        fil1.write(bytes)
    else:
        break
fil.close()
fil1.close()

"""
