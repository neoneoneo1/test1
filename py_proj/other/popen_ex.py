#Рабочий вариант
#комманды shell выполняются с shell=True
#Процессы выполняются с shell=False
import string, subprocess, os,sys
#fil=open("c:/outfile.txt", "w")
p_awk = subprocess.Popen(['Python','c:/py_proj/popen_ex1.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
#p_awk = subprocess.Popen(['dir','c:\\'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
#ss = p_awk.stdout.read()
#print ss
ss = p_awk.communicate()[0]
print repr(ss)
ss=ss.decode('cp1251')
print ss
#print repr(ss)#'stdout:', repr(ss)

#subprocess.STDOUT
#subprocess.PIPE
#p_awk = subprocess.Popen(['Python','c:/py_proj/popen_ex1.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True) 
"""
p_awk = subprocess.Popen(['echo','ok'],stdin=subprocess.PIPE, stdout=fil,shell=True) 
p_awk = subprocess.Popen(['dir','c:\\'],stdin=subprocess.PIPE, stdout=fil,shell=True) 
p_awk = subprocess.Popen('mspaint',stdin=subprocess.PIPE, stdout=fil) 
"""

#ss=p_awk.communicate('ok')
#p_awk.stdout.flush()

#p_awk.stdout.flush()


#ss=p_awk.communicate('ok')
#print p_awk.stdin
#p_awk.communicate('input data') 
#Ожидание завершения процесса
#p_awk.wait()
#fil.close()


#import string, subprocess, os
"""
from subprocess import Popen, PIPE 
import string, os
in1=0
out1=0
err1=0
#Так работает
sts = subprocess.call('mspaint c:/1.bmp', shell=True,cwd='c:/')
if sts == 0:
    print 'Проверка прошла'
else:
    print 'dpkg возвращает ошибку'
#sts = subprocess.call(['dpkg', '-i', '/tmp/new-package.deb'])
#sts = subprocess.call(['mspaint', '/1.bmp'])
"""



#po=subprocess.Popen('dir',shell=True,stdin=in1,stdout=out1,stderr=err1,args='c:/')
#print out1
#po=subprocess.Popen('dir c:/',shell=True,stdin=in1,stdout=out1,stderr=err1)
#po=subprocess.Popen(['dir','c:/'])#,stdin=PIPE,stdout=PIPE,stderr=PIPE)
#,shell=True,stdin=in1,stdout=out1,stderr=err1)
#p = subprocess.Popen([r'dir','c:/'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
#p.stdin.write('one\ntwo\nthree\nfour\nfive\nsix\n')
#p.communicate()[0]
#'four\nfive\n'
#p.stdin.close()
"""
call() - указатель, который передаёт свои параметры к конструктору Popen, который ожидает команду, чтобы завершить, и вернуть код состояния подпроцесса. Эта функция может служить более безопасным аналогом по отношению к os.system ():

sts = subprocess.call(['dpkg', '-i', '/tmp/new-package.deb'])

if sts == 0:

    # Проверка прошла

    ...

else:

    # dpkg возвращает ошибку

    ...

   Команда вызвана без использования оболочки. Если Вы действительно хотите использовать оболочку, Вы можете добавить shell=True как параметр ключевого слова и подставить строку вместо последовательности:

sts = subprocess.call('dpkg -i /tmp/new-package.deb', shell=True)

   PEP располагает различными примерами оболочки и кода Python и показывает, как они были бы оттранслированы в код Python, что использоваться в подпроцессах. Чтение этого раздела PEP строго рекомендуется.

Смотрите также:
"""

"""
args, bufsize=0, executable=None,
	    preexec_fn=None, close_fds=False, 
	    cwd=None, env=None, universal_newlines=False,
	    startupinfo=None, creationflags=0)
"""
"""
r,w,e=popen2.popen3("dir c:/")
rlines=r.readlines()
print rlines

class Popen(args, bufsize=0, executable=None,
	    stdin=None, stdout=None, stderr=None,
	    preexec_fn=None, close_fds=False, shell=False,
	    cwd=None, env=None, universal_newlines=False,
	    startupinfo=None, creationflags=0):

   args - обычно последовательность строк, которые будут параметрами к вызываемой программе, выполняющейся как подпроцесс. (Если параметр оболочки TRUE, параметрами может быть строка, которая будет тогда передана оболочке для интерпретации, также, как это делает os.system().)

   stdin, stdout, и stderr определяют, куда будет происходить ввод подпроцесса, вывод, и сообщения об  ошибках. Вы можете предоставить файловый объект или описатель файла, или Вы можете использовать константу subprocess.PIPE, чтобы создать канал между подпроцессом и родителем.

Конструктор имеет множество удобных вариантов:

    close_fds запрашивает, чтобы все описатели файла были закрыты перед выполнением подпроцесса.

    cwd определяет рабочий каталог, в котором подпроцесс будет выполняться (если не выполняется условие, что используется рабочий каталог родителя).

    env - словарь, определяющий переменные среды.

    preexec_fn  - функция, которую вызывают прежде, чем начат подпроцесс.

    universal_newlines открывает использование ввода и вывода подпроцесса, как  универсальную особенность новой строки в Python.

   Как только Вы создали экземпляр Popen, Вы можете вызвать его метод wait(), чтобы сделать паузу, пока подпроцесс не закончился, вызвать метод poll() для проверки выхода из него без приостановки, или communicate(data), чтобы послать строковые данные стандартному вводу подпроцесса. communicate(data) тогда читает любые данные, которые подпроцесс послал его стандартному выводу или стандартной ошибке, возвращая кортеж (stdout_data, stderr_data).

fin, fout = subprocess.Popen(
fout.write("foo\n")
fout.write("bar\n")
fout.close()

print fin.readline(),
print fin.readline(),
fin.close()
"""

