import random
import math
import socket
import select
import sys

#establish conn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 12346
s.bind(('', Port))
s.listen(5)

conn, addr = s.accept()
#send r
p = int(conn.recv(1024).decode())
conn.send(("1").encode())
g = int(conn.recv(1024).decode())
conn.send(("1").encode())
r0 = int(conn.recv(1024).decode())

z = random.randrange(1,p,1)
r = (g**z)%p
conn.send(str(r).encode())

#recieve r0

r1 = (r0**z)%p
print(p)
print(g)
print(r)
print(r0)
print(r1)

s.close()
