# -*- coding: utf-8 -*-
__author__ = 'admin'

#Классы
#Первый параметр всегда ссылка на сам объект
#а со второго и далее входные параметры в определении
#функции класса
class MyClass:
    "Пример класса"
    i=123
    def __init__(self): #Это конструктор
        print "конструктор"
    #Объекты с переопределенным методом del gc(сборщик мусора не удалит сам)
    def __del__(self): #Это деструктор
        print "деструктор"
    def __init__(self,par1): #Это конструктор с параметрами
        print "конструктор с параметрами",par1
    def f1(self,x1):    #Это функция член-класса
        print x1
        return "return функции"

x=MyClass(22)
print x.f1(1)



#Вызов метода не привязанного к объекту
#В данном случае надо передать первым аргументом имя объекта
#аля self
ss=MyClass.f1(x,1)
print ss
del x

#Можно определеить функцию вне класса и потом
#внутри класса присвоить её имени
def outFun(self,x,y):
    return x+y
#В классе будет 3 функции f,g,h
class C:
    f=outFun
    def g(self):
        return "Ещё функция"
    h=g


#Методы могут вызывать другие методы как атрибуты аргумента self
class Bag:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)

#Наследование
#class производный_класс(модуль.базовый_класс)
class A:
    def __init__(self):
        print "Конструктор А"
    def funA(self,x):
        print 'funA из A класса x=',x

class B(A):
    def __init__(self):
        A.__init__(self) #Вызов конструктора унаследованного класса
        print "Конструктор B"
    def funB(self,x):
        print 'x=',x
    def funA(self,x):   #Переопределение метода базового класса
        print 'Перегруженный funA из B класса x=',x
        #Вызов такой же функции базового класса
        A.funA(self,x)
bb=B()
bb.funA(2)
bb.funB(3)


#Множественное наследование
#Поиск атрибута проходит сначала в порожденном классе
#Если на аттрибут не найден далее поиск идет в base1
#Затем рекурсивно внутри базовых классов base1
#Затем в base2  и т д.
class base1:
    def __init__(self):
        pass #заменитель пустых {} в c++
    i=1
class base2:
    def __init__(self):
        pass #заменитель пустых {} в c++
    i=10
class derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
class derived1(base2,base1):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
x=derived()
y=derived1()
print x.i, y.i

#Частные атрибуты
#Частные аттрибуты должны начинаться с двух подчерков (минимум)
#вначале и не более одного в конце заменяется на
#_класс__атрибут и указывает на то что параметр частный
class test:
    def __init__(self):
        pass
    def __fun_(self):
        print "Частный метод"
    __s_="Частный параметр"
    i=10
    def fun1(self):
        self.__fun_()
x=test()

#Доступ к частным атрибутам есть
#Но использовать их можно только из методов класса
#или как члены объектов класса (не совсем понятно)
#Производные классы как бы не могут их переопределить
#Потому что имя частного атрибута меняется, туда добавляется
#префиксом имя текущего класса
#Есть ограничение на общую длину 255 символов
#Бля теперь понятно
x._test__fun_()
print x.i,x._test__s_

class test1(test):
    def __init__(self):
        test.__init__(self)
    def __fun_(self):
        print "Попытка перегрузки частного метода"
    def fun1(self):
        self.__fun_()
x=test1()
x.fun1()


#Структыры как в C = пустой класс
class Emploee:
    pass

j=Emploee()
j.name="Появилось поле name"
j.zp="Появилось поле zp"
print j.name


#Паралельнй перебор элементов двух последовательностей
#с помощью класса, последовательность закончиться с исключением
#IndexError, если его не обрабатывать то все пройдёт тихо
class parallel:
    def __init__(self,*args):
        self.__args=args
    def __getitem__(self,item): #какая-то неведомая хуйня
        return map(lambda s,i=item: s[i], self.__args)
seq1=xrange(10)
seq2=[1,2,3,5,7]
for x,y in parallel(seq1,seq2):
    print x,y


#Контроль доступа к атрибутам
#с помощью __getattr__(), __setattr__(), __delattr__()
#можно контролировать все обращения к атрибутам экземпляра
"""#Работает но затрахало вылезать в самом конце
class vv:
    __vdict=None
    #Получить преобразованное имя атрибута __vdict:
    __vdict_name='_vv__vdict' #locals().keys()[_vv__vdict]

    def __init__(self):
        self.__dict__[self.__vdict_name]={}

    def __getattr__(self,name):
        print "__getattr__"
        return self.__vdict[name]

    def __setattr__(self,name,value):
        print "__setattr__"
        self.__vdict[name]=value
    def __delattr__(self):
        print "__delattr__"
x=vv()
x.rr=1
"""
#print x.rr

#Возвращает id (идентификатор) объекта
class MyClass:
    pass
x=MyClass()
i=MyClass()
print id(x),id(i)
class MyClass1(MyClass):
    pass
#ввод стандартный аля raw_input
#x=input('Введи:')
#print x

#Вернёт 1 если x является объектом класса MyClass
print isinstance(i,MyClass)

#Вернёт 1 если subClass унаследован (даже косвенно) от класса MyClass
print issubclass(MyClass1,MyClass)

