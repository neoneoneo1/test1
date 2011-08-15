import zlib, gzip, bz2, tarfile, zipfile, os
#работа с архиваторами
s='this is a string\nthis is a string\nthis is a string\nthis is a string\n'
print len(s)
s=zlib.compress(s)
print len(s)
s=zlib.decompress(s)
print s,'crc32=',zlib.crc32(s)


#Пример tar-а

#Запаковка в tar.bz2
tf=tarfile.TarFile(name='c:/py_proj/ar.tar.bz2',mode='w')
tf.add('c:/py_proj/array_ex.py','arr.txt')
tf.add('c:/py_proj/array_ex.py','array_ex.py')
tf.close()

#Запаковка в tar
tf=tarfile.TarFile(name='c:/py_proj/ar.tar',mode='w')
tf.add('c:/py_proj/array_ex.py','arr.txt')
tf.add('c:/py_proj/array_ex.py','array_ex.py')
tf.close()

#блять gzip  умеет архивировать только 1 файл
#поэтому надо tar-ить
fil1=open('c:/py_proj/ar.tar','rb')
fil_gz=gzip.open('c:/py_proj/arr.tar.gz','w')
fil_gz.writelines(fil1)
fil_gz.close()
fil1.close()

#Распаковка архива
tf=tarfile.TarFile(name='c:/py_proj/ar.tar.bz2',mode='r')
tf.extractall('c:/py_proj/s')
tf.close()

