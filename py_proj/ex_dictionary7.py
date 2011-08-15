# -*- coding: utf-8 -*-
__author__ = 'admin'
#Словарь (ассоциативный массив)
#Плохо работает с юникодом
dict={1:"адын",2:'two',3:'three',4:'four'}
print dict

#Получитьв все ключи
print dict.keys()

#Есть ли такой ключ
print dict.has_key(1)

#Удалить элемент по ключу
del dict[1]
print dict

#Добавление в словарь пары (ключ-значение)
dict[5]='five'
print dict

table={'str1':123,'str123':1,'str45':12}
for name,phone in table.items():
    #-10s 10 символов с выравниванием по левому краю
    #10s 10 символов с выравниванием по правому краю
    print '%-10s ==> %10d' % (name,phone)

#Чтоб не искать значения по позициям пожно юзать словарь
tab={'first':123,'second':321,'third':111}
print 'first:%(first)d; second:%(second)d; third:%(third)d;' %tab

#Словарь описывается в {} скобках
keys={'one1':11,'two1':22,'three1':33}
apply(tmpf1,args,keys)

#Словари
#Количество пар
s={1:'v1',2:'v2',3:'v3'}
print len(s)
#Выдает значение по ключу, если не находит выдает исключение
print s[1]
s[1]='1v'#замена значения
print s
#Удаление пары
del s[1]
print s
#Зачистка словаря
s.clear()
#Возвращает 1 если ключа найден
s={1:'v1',2:'v2',3:'v3'}
print s.has_key(1)
#Возвращает последовательность пар списков (ключ, знчеине)
print s.items()
#Тоже получение значения по ключу
print s.get(1)

