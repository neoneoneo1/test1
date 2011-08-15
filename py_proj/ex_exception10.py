# -*- coding: utf-8 -*-
__author__ = 'admin'
#Если исключение не обработано, не по типу, выполнение прерывается
#выводиться сообщение об ошибке
"""Надоело вводить цифру
while 1:
    try:
        x=int(raw_input("Введите целое: "))
        break
    except ValueError:
        print "Ещё раз..."
    except (RuntimeError,TypeError, NameError,IOError,exc):
        #отловить остальные и пропустить
        #чтоб не прерывать выполнение
        pass
    #except : #отлов всех исключений не рекомендуется, перекроет системные
        raise #Повторно генерирует последнее исключение
    else:
        print "Исключения не генерируются всё ок"
print "end"
"""

#Можно исключению передать параметр
try:
    spam()
except NameError, x:
    print 'Имя',x,'не определено'

#Обработчик так же ловит исключения в генерируемых функциях
def this_fails():
    x=1/0
try:
    this_fails()
except ZeroDivisionError,exc:
    print "Ошибка времени выполнения:",exc
finally:
    print "finally" #Выполняется при любом раскладе


try:
    raise NameError('Принудительно сгенеринное исключение')
except NameError:
    print "Исключение получено"





#После ключевого слова except могут быть перечислены
#как строки так и классы. Указанный класс считается совместимым
#с исключением, если исключение является экземпляром этого класса или класса,
#производного от него (но не наоборот - если в ветви except указан производный
#класс от того, экземпляром которого является исключение, то исключение
#не обрабатывается.
#Не понимаю
class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B,C,D]:
    try:
        raise C()
    except D:
        print 'D'
    except C:
        print 'C'
    except B:
        print 'B'
#Если расположить ветви except наоборот в обратном порядке. то получишь B B B
#Сработает первая ветвь except, совместимая с исключением.

#Определение своего исключения с помощью класса Exception
class MyError(Exception):
    pass
#raise MyError('oops') #Вызов исключение

#Типы полезных исключений унаследованный от класса Exception
"""
FloatingPointError - ошибки операций с числами с плавающей точкой

OverflowError - переволнение числа в рамках заданного типа

ZeroDivisionError - деление на ноль

AssertionError - если не выполняется условие заданное assert()

AttributeError - если нельзя получить значение атрибута print x.u

EOFError -  генерируется методами input, raw_input если досигнут конец файла,
            а из файла ничего не считано

EnvironmentError - исключения возникающие вне среды питона

IOError - ошибка ввода вывода, не найден открываемый файл, нет места на диске...

WindowsError - выдается только в windows, содержит errno из winapi

ImportError - ошибка при импорте модуля, или модуль не найден

KeyboardInterrupt - Ctrl+C (SIGINT)

IndexError - индекс вышел за пределы диапазона

KeyError - Если не найден элемент по ключу

MemoryError - Если не хватает памяти для операции

NameError - Если пытаешься вывести необъявленную и
            не инициализированную переменную

UnboundLocalError - при попытке сослаться на глобальную переменную без global

RuntimeError - ошибки времени выполнения не попадающие ни под одну известную

NotImplementedError -   для показа что метод класса абстрактный
                        и его надо перегрузить

SyntaxError - Ошибки при использовании eval exec input и т д

SystemError - внутренняя ошибка питона

TypeError - если операция применяется к объекту несоответствующего типа

ValueError -    если операция применяется к объекту соответствующего типа
                но имющего несоответсвующее значение

UnicodeError - если есть ошибки преобразования в/из юникода

SystemExit -    генериться если вызывается sys.exit()
                в дочернем процессе пользовать os._exit()
"""
