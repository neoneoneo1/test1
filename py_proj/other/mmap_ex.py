import mmap

# write a simple example file
f=open('c:/hello.txt','w')
f.write('Hello Python!\n')
f.close()

f=open('c:/hello.txt', 'w+')
# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print mm.readline()  # prints "Hello Python!"
# read content via slice notation
print mm[:5]  # prints "Hello"
# update content using slice notation;
# note that new content must have same size
#mm[6:] = ' world!\n'
#mm.write('okokok')
#mm[6:] = 'world!\n'
# ... and read again using standard file methods
mm.seek(0)
print mm.readline()  # prints "Hello  world!"
# close the map
mm.close()
f.close()






"""
import mmap
fd=open('c:/123.txt','w')
a=mmap(fd,3)
a.append(10)
fd.close()
"""

# import mmap
# import os
# 
# map = mmap.mmap(-1, 13)
# map.write("Hello world!")
# 
# pid = os.fork()
# 
# if pid == 0: # In a child process
#     map.seek(0)
#     print map.readline()
# 
#     map.close()
# 