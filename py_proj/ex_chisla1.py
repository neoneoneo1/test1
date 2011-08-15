# -*- coding: utf-8 -*-
"""
Многострочный комент
явное указание кодировки файла
# -*- coding: cp1251 -*-
# -*- coding: utf-8 -*-
"""

#типы данных int, long int, float, complex
#int от -2147483647 до 2147483647
#long int не ограничены
#0xFF-шестнадцетиричная запись
#0340-восьмеричная запись


#Путь или имя файла не должно быть на русском языке иначе кирдык редактору
import string
import os

print 2+2#Числа
#Возвращает целое после floor
print 'результат целый 7/3:',7/3   #результат целый
print 'результат float 7.0/3:',7.0/3 #результат float

#Инициализация выражением
var1=30*40
print 'Инициализация выражением var1=30*40:',var1

#Множественное присваение
var1=10
var3=var2=var1
print 'Множественное присваение var3=var2=var1:',var1,var2,var3

#Комплексные числа
#Первый способ объявления
vv=10+11j
print 'Комплексные числа 1й способ объявления vv=10+11j:',vv
print 'Целая часть:',vv.real
print 'Мнимая часть:',vv.imag


#Второй способ объявления
vv=vv*complex(10,11)
print 'Комплексные числа 2й способ объявления vv=vv*complex(10,11):',vv
print 'Целая часть:',vv.real
print 'Мнимая часть:',vv.imag
print 'Абсолютное значение комплексного числа abs(vv):', abs(vv)

#приведение к типам
print 'int(10):',int(10)
print 'long(10):',long(10)
print 'float(10.12):',float(10.12)
print 'str(10.12):',str(10.12)

#Если строка содержит только цифры вернет 1
s="01234"
print 's.isdigit():',s.isdigit()

#Для строк Unicode
#вернёт 1 если в строке только десятичные цифры (не только из ascii)
s=u"2344"
print 's.isdecimal():',s.isdecimal()

#вернёт 1 если в строке только числа в том числе и римские
s=u"123"
print 's.isnumeric():',s.isnumeric()

#Множественное присвоение как у руби
a,b=1,2
print "a,b=1,2:",a,b

#округляет число цифр после десятичной точки
print "округляет число цифр после десятичной точки round(1.12345,3):",round(1.12345,3)

import math
x=math.floor(1.5)
print x
x=math.ceil(1.5)
print x

  