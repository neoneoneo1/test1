# -*- coding: utf-8 -*-
__author__ = 'admin'
#Модуль Сборщик мусора
import gc

#Включение
gc.enable()
#Выключение
gc.disable()
#Если включен
if not gc.isenabled():
    gc.enable()
#Запуск сборки мусора вернёт количество найденных объектов
#Список объектов которые невозможно прибрать будет в переменной garbage
gc.collect()
print gc.garbage
#Установка вывода отладочной инфы. отключается через set_debug(0)
#get_debug() - текущий уровень отладки
gc.set_debug(gc.get_debug())

#Устанавливает пороги запуска (частоту) автоматического "сбора мусора"
#thr=0 - отключает автоматическую сборку мусора
#gc.set_threshold(thr,thr1,thr2)
#gc.get_threshold() - вернёт кортеж 3х количеств поколоений объектов
thr=0
gc.set_threshold(thr)

#Флаги для отладки
#Выводить инфу по найденным недоступным объектам которые надо удалить
gc.DEBUG_COLLECTABLE=1
#Если стоит DEBUG_COLLECTABLE или DEBUG_UNCOLLECTABLE
#Выдает инфу по экземплярам классов
gc.DEBUG_INSTANCES=1
#Полезен при утечках памяти
gc.DEBUG_LEAK=1
#Если стоит DEBUG_COLLECTABLE или DEBUG_UNCOLLECTABLE
#Выдает инфу по объектам не членам классов
gc.DEBUG_OBJECTS=1
#Все найденные недоступные объекты даже те которые можно удалить будут
#сохранятся - отправляться в garbage
gc.DEBUG_SAVEALL=1
#Выводить статистику при запусках сборщика мусора
gc.DEBUG_STATS=1
#Выводить инфу по найденным недоступным объектам которые невозможно удалить
gc.DEBUG_UNCOLLECTABLE=1

