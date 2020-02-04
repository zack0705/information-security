import random
import math
import socket
import select
import sys

def generate_prime():
	q = 1
	p = 2
	while(q==1 and p>1):
		p = random.random()*1000
		p = int(p//1)
		q = 0
		for i in range(1,int(math.sqrt(p))):
			if(p%(i+1) == 0):
				q = 1
				break
	return p
	
def select_g(p):
	c = 0 
	while(c != p):
		g = random.randrange(1,p-2,1)
		x = (g*g)%p
		c = 2
		while(g!=x):
			x = (g*x)%p
			c += 1 
	return g
	
def gcd(a,b):
	t1 = 0
	t2 = 1
	r1 = b
	r2 = a
	
	while(r2!=0):
		q = int(r1/r2)
		r = r1%r2
		r1 = r2
		r2 = r
	
		t = t1 - (q*t2)
		t1 = t2
		t2 = t
		
	return(r1)
	
p = generate_prime()
g = select_g(p)
z = random.randrange(1,p,1)
r = (g**z)%p

#establish conn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '127.0.0.1'
Port = 12346
s.connect((IP_address, Port))

s.send(str(p).encode())
s.recv(1024).decode()
s.send(str(g).encode())
s.recv(1024).decode()
#send r

s.send(str(r).encode())

#recieve r0

r0 = int(s.recv(1024).decode())

r1 = (r0**z)%p
print(p)
print(g)
print(r)
print(r0)
print(r1)

s.close()
