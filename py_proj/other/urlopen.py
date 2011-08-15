import os, smtplib
import urllib as ur
for line in ur.urlopen(url='http://127.0.0.1/'):
    print line.decode('cp1251')
    
fp=open('c:/py_proj/1.html','w')
for line in ur.urlopen(url='http://127.0.0.1/phpma'):
    fp.write(line.decode('cp1251'))
    #print line.decode('cp1251')
#os.system('"C:\\Program\ Files\\Mozilla\ Firefox\\firefox.exe \'c:\\py_proj\\1.html\'"')
#os.system('"C:/Program Files/Mozilla Firefox/firefox.exe c:/py_proj/1.html"')
#os.system('firefox.exe \'c:\\py_proj\\1.html\'')
#os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe c:\\py_proj\\1.html"')
#os.system('"C:/Program Files/Mozilla Firefox/firefox.exe c:/py_proj/1.html"')
#os.system('c:/py_proj/1.html')
fp.close()



# serv1=smtplib.SMTP('localhost')
# serv1.sendmail('to@microsoft.com','from@microsoft.com',
# """To: to@microsoft.com
# From: to1@microsoft.com
# 
# Beware the Ides of March.
# """)
# serv1.quit()
# 

