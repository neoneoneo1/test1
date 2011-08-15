# -*- coding: utf-8 -*-
__author__ = 'admin'
#Вызов из другого файла
if os.path.isfile('C:/py_proj/init.py'):
    execfile('C:/py_proj/init.py')

#Исполнение файла
#import os
#os.system("\"c:\\windows\\system32\\notepad.exe\"")

#Привязывает домен к папке где хранятся переводы
#После чего gettext будет искать переводы в двоичном файле
#по пути
#os.path.join('c:/Python/share/locale',language,'LC_MESSAGES',domain+'.mo')
