# -*- coding: utf-8 -*-
__author__ = 'admin'
#Модуль atexit - выполнение действий при окончании работы программы
import atexit
def funOnExit(p):
    #print p
    fil=open("c:/test1.txt","w")
    fil.write("ok")
    fil.close()
p="Вышли"
atexit.register(funOnExit,p)
#sys.exit() # работает бля


#Получение типа
import types
x="ddgdf"
if type(x) == types.StringType:
    print "Объект строка"
print type(x)

#Возвращает словарь текущего пространства имен
#print vars('x')


import types
i=10
if type(i)==types.IntType:
    print 'i - int type'

"""
Доступные типы
NoneType
TypeType
IntType
LongType
FloatType
ComplexType
StringType
UnicodeType
TupleType
XRangeType
BufferType
ListType
DictType
DictionaryType
FunctionType
... и т д
"""


#и т д

import traceback
#Вывод уровней информации для объекта (наверное объекта класса или переменной)
#от исключения назад на N уровней
#i=10/0
#traceback.print_tb(i,10)
#вобщем это нам пока не надо


#Выдача сообщений на родном языке
import gettext
#для многоязычности
#Выдает сообщение с переводом по базе по нац. установкам
print gettext.gettext("Привет")
print gettext.locale.getlocale()
#Привязывает домен к папке где хранятся переводы
#После чего gettext будет искать переводы в двоичном файле
#по пути
#os.path.join('c:/Python/share/locale',language,'LC_MESSAGES',domain+'.mo')
#Если аргумент 'c:/Python/share/locale' равен None, вернёт текущий
#привязанный каталог
#os.path.join(sys.prefix,'share','locale')
gettext.bindtextdomain('domain','c:/Python/share/locale')

#Задает или возвращает домен
print gettext.textdomain()
#Получение сообщения для указанного домена
print gettext.dgettext('messages',"Сообщение")


#интерфейс на классах для gettext сделанный для удобства




#locale - модуль использования национальных особенностей
import locale
#Установка локали
#Всё глючит в пизду
#locale.setlocale(locale.LC_ALL,'')
#print locale.localeconv('decimal_point')
#print locale.getdefaultlocale(LC_ALL)
#print locale.getdefaultlocale(LANG)
#raw_input("ok")

#print locale.atof(1.001)
#print locale.atoi(1001)
#Продолжение в другом файле




