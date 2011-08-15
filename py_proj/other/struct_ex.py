import struct
"""
Character Byte order Size and alignment 
@ native native 
= native standard 
< little-endian standard 
> big-endian standard 
! network (= big-endian) standard 


Format C Type Python Notes 
x pad byte no value   
c char string of length 1   
b signed char integer   
B unsigned char integer   
? _Bool bool (1) 
h short integer   
H unsigned short integer   
i int integer   
I unsigned int integer or long   
l long integer   
L unsigned long long   
q long long long (2) 
Q unsigned long long long (2) 
f float float   
d double float   
s char[] string   
p char[] string   
P void * long 
"""

v=10
#x-пустышка внутри структуры размером в 1 байт
#Упаковка всех видов
ss=struct.pack('@chHiIlLqQfd10s10pPcxB','y',-32767,65535,-32768,65536,-1000000,10000000,-1000000000000,1000000000000,-0.001,1.1101,'0123456789','0123456789',v,'g',2)

#Простой пример с пустым байтом
ss=struct.pack('@cxh','y',-32767)
c,h=struct.unpack('@cxh',ss)
print c,h

#Простой пример с распаковкой и количестком пакуемых однотипных элементов
ss=struct.pack('@3c','0','1','2')
c1,c2,c3=struct.unpack('@3c',ss)
print c1,c2,c3

#Упаковка через аргументы функции - очень полезно
li=[1,2,3]
ss1=struct.pack('3i',*li)
l1,l2,l3=struct.unpack('3i',ss1)
print l1,l2,l3

#print 'Unpacked:', s.unpack_from(b, 0)
#Вычсление размера предполагаемой структуры по формату
print struct.calcsize('3i'),'байт'

