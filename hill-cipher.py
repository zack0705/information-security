import numpy as np
import math
import sys
import random

def possible(k1):
	k1 = int(k1)
	l = int(math.ceil(math.sqrt(float(k1))))
	
	m = np.ndarray(shape=(l,l), dtype="int")
	m[:] = 0
	for i in range(l):
		for j in range(l):
			m[i][j] = random.randint(97,122)
	det = np.linalg.det(m)
	z = inv(det)
	i=97
	j1=0
	j=0
	while(z==-1):
		m[j1][j] = i
		det = np.linalg.det(m)
		z = inv(det)
		i+=1
		if(i==122):
			i=0
			j+=1
			if(j==l):
				j=0
				j1+=1
				if(j1==l):
					print("no no no")
	k=""
	for i in range(l):
		for j in range(l):
			k += chr(m[i][j])
	print(k)

def inv(a):
	a = a%256
	a = round(a)
	t1 = 0
	t2 = 1
	b = 256
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
		
	x = (a*t1)%b
	if(x==1):
		return(t1%256)
	else:
		return(-1)

def generate_m(k):
	l = int(math.ceil(math.sqrt(len(k))))
	
	m = np.ndarray(shape=(l,l), dtype="int")
	m[:] = 0
	i = 0
	j = 0
	
	for a in k:
		m[i][j] = int(ord(a))
		if(j<l):
			j += 1
		if(j==l):
			i += 1
			j = 0
	a = 0
	while(i!=l):
		m[i][j] = a%256
		a += 1
		if(j<l):
			j += 1
		if(j==l):
			i += 1
			j = 0
	det = np.linalg.det(m)
	z = inv(det)
	return(m,z,l,det)

k1 = raw_input("enter length")
possible(k1)
k = raw_input("Enter key")
k,z,l,d = generate_m(k)
print(k,z,l)
if(z==-1):
	print("invalid key")
	sys.exit()

print("encrypt or decrypt")
a = raw_input()
if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	old = old[:-1]
	new = ""
	while(len(old)%l != 0):
		old += "z"
	for i in range(len(old)/l):
		x = np.ndarray(shape=(l,1), dtype="int")
		x[:] = 0
		j = 0
		for ki in range(l):
			x[j][0] = int(ord(old[int((l*i)+ki)]))
			j+=1 
		y = np.dot(k,x)
		for i in y:
			new += chr(int(i)%256)
	(open("sample_change.txt", 'w')).write(new)
elif(a=="decrypt"):
	old = (open("sample_change.txt")).read()
	new = ""
	k = np.linalg.inv(k)
	k = k*d*z%256
	m = np.ndarray(shape=(l,l), dtype="int")
	m[:] = 0
	for i in range(l):
		for j in range(l):
			k[i][j] = round(k[i][j]%256)
			m[i][j] = int(k[i][j])
	k = m
	for i in range(len(old)/l):
		x = np.ndarray(shape=(l,1), dtype="int")
		x[:] = 0
		j = 0
		for ki in range(l):
			x[j][0] = int(ord(old[int((l*i)+ki)]))
			j+=1 
		y = np.dot(k,x)
		for i in y:
			new += chr(int(i)%256)
	(open("sample_returns.txt", 'w')).write(new)
