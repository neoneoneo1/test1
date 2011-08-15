import os, string, shutil, glob, sys
#поулчение текущей папки
oldpath=os.getcwd()
print str(os.getcwd()).decode('cp1251')
#Смена текущей папки
os.chdir('c:/')
print str(os.getcwd()).decode('cp1251')
os.chdir(oldpath)
print str(os.getcwd()).decode('cp1251')
#команда system
#os.system('mspaint')


#Копирование одного файла
shutil.copyfile('c:/py_proj/test.txt','c:/py_proj/s/test1.txt')
if os.access('c:/py_proj/d',os.R_OK):
    #Удаление пустых папок
    #os.rmdir('c:/py_proj/d')
    #Удаление НЕ пустых папок
    shutil.rmtree('c:/py_proj/d')
if os.access('c:/py_proj/d1',os.R_OK):    
    shutil.rmtree('c:/py_proj/d1')
#Копирует папку вместе с подкаталогами и файлами
shutil.copytree('c:/py_proj/s','c:/py_proj/d')
#Переносит/переименовывает папку/файл если такой имеется и не пуст получишь исключение
#shutil.move('c:/py_proj/d','c:/py_proj/d123')
#shutil.move('c:/py_proj/d123/test1.txt','c:/py_proj/d123/test2.txt')
os.chdir('c:/py_proj')
#Выделение файлов по маске
print glob.glob('*.py')
#Список аргументов в виде массива
print sys.argv
#Запись в стандартный поток ошибок
sys.stderr.write('ok\nok\nok')

