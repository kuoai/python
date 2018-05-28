import socket
host=""
port="10086"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("链接到的IP地址是：",addr)
while 1:
    data=conn.recv(1024)
    if not data:break
    print("客户端发过来的数据是:",repr(data))
    conn.sendall(data.upper())
conn.close()