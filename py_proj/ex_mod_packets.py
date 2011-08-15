# -*- coding: utf-8 -*-
__author__ = 'admin'
#3 варианта импорта модуля
from init2 import fff
#import init2
#from init2 import *
x=fff(2)
print x

#чтобы функцию нельзя было импортировать через  from init2 import *
#можно переименовать функцию чтоб имя начиналось с _
#и удалить старую ссылку на имя
#import string
_fff = fff
del fff

#Можно импортировать с другим именем
#import fff as _fff
#from init2 import fff as _fff

#Если имя импортируемого модуля становиться известным
#только во время выполнения то можно пользоваться exec
module_name='init2'
exec("exec 'import '+module_name")
#или
#встроенной функцией __import__()




#Пакеты - сборники модулей
#Последняя единица должна быть модулем или пакетом
#import пакет.пакет.модуль или пакет
#from пакет.пакет или модуль или функция или класс или переменная import myfunf1
from paket.mymod import myfunf1
#from paket.mymod import *
#import paket.mymod
print myfunf1(3)

#Когда пакеты разделены на подпакеты () пакет Sound например,
#нет краткой записи для ссылок между ответвлениями пакета -
#нужно использовать полное имя. Например
#если модуль Sound.Filters.vocoder должен использовать модуль echo
#из пакета Sound.Effects, нужно использовать
#from Sound.Effects import echo




