#винсок
import socket
#Локальный узел
HOST=''
PORT=50007

#Сервер
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print 'Подсоединились с адреса', addr
while 1:
    data=conn.recv(1024)
    if not data:
        break
    else:        
        print "Данные от клиента", data
    conn.send("from serv to client")
conn.close()
