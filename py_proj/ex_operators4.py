# -*- coding: utf-8 -*-
__author__ = 'admin'
#Условия if
i=10
if i==10 :
    print "ok 10"
elif i==11:
    print "ok 11"
else:
    print "ok other"

#Оператор break, continue присутствуют
a=[1,2,3,4,5,6,7,8,9]
for x in a:
    if x>5:
        break
    else:
        print x

i=0
while i<10:
    i=i+1
    print i
else:
    #Выполняется 1 раз когда while закончился
    print "Выход за пределы"

"""долго ждать влом работает ток медленно
s=0
for i in xrange(10000000):
    s=s+i
print s
"""

#Как бы наполнение списка
def funadd(item=None):
    if item is None:
        item=["first el"]
    else:
        item.append("el-t")
    return item
i=funadd()
print i
i=funadd(i)
i=funadd(i)
print i


#Проверка x in s 1 если x входит в последовательность s
x=1
if x in xrange(3):
    print "ok"
#Сишные операторы работают кроме ++ --
x+=1
x*=2

print "min(1,2),max(1,2):",min(1,2),max(1,2)

global glob_var1
glob_var1="Глобальная переменная, используется только после указания global"
print glob_var1


a=1
if a<11 and \
a>0 or \
a==10:
    print "ok"

#eval работает как во флеше
x=10
print "eval работает как во флеше eval('x+1'):",eval('x+1')

#Битовые операции
i=0
i|=0x03
print i
if i & 0x02 :
    print "ok"

#Цикл while
i=0
while i<10 :
    i=i+1
    print i

def fun1():
    print "ok"

bit=1
for i in range(0,9):
    bit=bit<<1
    print bit
    i=i+1

#Хитрые условия
#in и not in проверяют есть ли указанное значение в последовательности
#или нет
#is и is not определяют ссылаются ли две переменные на один и тот же объект
#Хитрые логические
a=10
if 10==a<100:
    print a
a=True
b=True
c=True
#Проверяется справа налево
if a or not b and c: #a or ((not b) and c)
    print a
else:
    print b,c

#сравнения последовательностей
print (1,2,3)<(1,2,4)
print [1,2,3]<[1,2,4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1,2,3,4) < (1,2,4)
print (1,2) < (1,2,-1)
print (1,2,3) == (1.0,2.0,3.0)
print (1,2,('aa','ab')) < (1,2,('abc','a'),4)

#Форматированный вывод
#Длинное целое число
print str(1000L) #Приведение к строке
print repr(1000L)#Приведение к строке
print oct(1000)#Строковое представление числа в восьмеричке
print hex(1000)#Строковое представление числа в хексе
print `1000L`+'123'#Приведение к строке

#Оператор %
import math
print "Значение PI=%5.3f" % math.pi

#про labmda
n=2
g=lambda x:x**n #аналогично x в степени 2
print 'lambda=',g(2)

#Взятие по модулю
print abs(-10)

#и так для большинства встроенных функций
x=1
print x.__lshift__(1) #Аналог оператора <<

import operator

class MyClass:
    par1=10
x=MyClass()
x.par1=operator.add(x.par1,x.par1) #Возвращает x+x
print x.par1

#перегрузить модуль снова
reload(os)
