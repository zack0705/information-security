import numpy as np

def key_change_enc(key):
	l = []
	p = []
	for i in key:
		l.append(ord(i))
		p.append(ord(i))
	p.sort()
	
	for i in range(len(p)):
		for j in range(len(l)):
			if(p[i]==l[j]):
				l[j] = i+1
				break
	return l
		
def key_change_dec(key):
	l = []
	p = []
	for i in key:
		l.append(ord(i))
		p.append(ord(i))
	p.sort()
	for i in range(len(l)):
		for j in range(len(p)):
			if(l[i]==p[j]):
				p[j] = i+1
				break
	return(p)

def encrypt(old,key):
	while(len(old)%len(key) != 0):
		old += "z"
	m = np.chararray([len(old)/len(key), len(key)])
	m[:] = "-"
	n = np.chararray([len(old)/len(key), len(key)])
	n[:] = "-"
	
	i=0
	j=0
	p=0
	for i in range(len(old)/len(key)):
		for j in range(len(key)):
			m[i][j] = old[p]
			p+=1
	new = ""
	for j in range(len(key)):
		for i in range(len(old)/len(key)):
			new += m[i][int(key[j])-1]
			n[i][j] = m[i][int(key[j])-1]
	return(new)

def decrypt(old,key):
	m = np.chararray([len(old)/len(key), len(key)])
	m[:] = "-"
	n = np.chararray([len(old)/len(key), len(key)])
	n[:] = "-"
	
	i=0
	j=0
	p=0
	for j in range(len(key)):
		for i in range(len(old)/len(key)):
			m[i][j] = old[p]
			p+=1
	for j in range(len(key)):
		for i in range(len(old)/len(key)):
			n[i][j] = m[i][int(key[j])-1]
	new=""
	for i in range(len(old)/len(key)):
		for j in range(len(key)):
			new += n[i][j]
	return(new)

	

print("encrypt or decrypt")
a = raw_input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	old = old[:-1]
	
	alpha = "abcdefghijklmnopqrstuvwxyz0123456789.,/<>?;:{}[]=-+_)(*&^%$#@!~`QWERTYUIOPASDFGHJKLZXCVBNM"
	new = ""
	for i in old:
		if i in alpha:
			new += i
		if(i==" "):
			new+="_"
	old = new
	
	new = ""
	k = raw_input("enter key")
	
	k = key_change_enc(k)
	
	new = encrypt(old, k)
	
	(open("sample_change.txt", 'w')).write(new)
	
elif(a=="decrypt"):
	old = (open("sample_change.txt")).read()
	new = ""
	k = raw_input("enter key")
	k = key_change_dec(k)
	new = decrypt(old,k)
	new1 = ""
	for i in new:
		if(i=="_"):
			new1+=" "
		else:
			new1+=i
	(open("sample_returns.txt", 'w')).write(new1)
	

