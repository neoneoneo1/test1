#Скрипт создает в текущей папке scr.py записывает туда код питона и выполняет
#передавая ему аргументы
#тот скрипт получает аргументы и печатает их в файл scr1.py
import sys, os, subprocess, string
#поулчение текущей папки
cur_path=os.getcwd()
text_scr="\
import os,sys\n\
cur_path=os.getcwd()\n\
fil=open(cur_path+'\\\\scr1.py','w')\n\
for i in sys.argv:\n\
    fil.write(str(i)+'\\n')\n\
fil.write(str(len(sys.argv)))\n\
fil.close()\n\
"
fil=open(cur_path+'\\scr.py','w')
fil.write(text_scr)
fil.close()
pk = subprocess.Popen(['C:\\Python26\\python.exe',cur_path+'\\scr.py','arg1','par2'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
ss = pk.communicate()[0]
print 'end'
