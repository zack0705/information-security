import numpy as np

def tab(a):
	m = np.chararray([6,6])
	m[:] = "a"
	n = ""
	i = 0
	j = 0
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
	for k in a:
		if(k not in n and k != " " and k in alphabet):
			m[i][j] = k
			n += k
			if(j==5):
				i+=1
				j=0
			else:
				j+=1
	for k in alphabet:
		if(k not in n and k != " "):
			m[i][j] = k
			n += k
			if(j==5):
				i+=1
				j=0
			else:
				j+=1
	return m

key = raw_input("enter key")
key_tab = tab(key)
print(key_tab)


def transform(a,b,key):
	ai=0
	aj=0
	bi=0
	bj=0
	for i in range(6):
		for j in range(6):
			if(key[i][j] == a):
				ai = i
				aj = j
			if(key[i][j] == b):
				bi = i
				bj = j
	send = ""
	if(ai==bi):
		send = key[ai][(aj+1)%6] + key[bi][(bj+1)%6]
	elif(aj==bj):
		send = key[(ai+1)%6][aj] + key[(bi+1)%6][bj]
	else:
		send = key[ai][bj] + key[bi][aj]
	return send
	
def reform(a,b,key):
	ai=0
	aj=0
	bi=0
	bj=0
	for i in range(6):
		for j in range(6):
			if(key[i][j] == a):
				ai = i
				aj = j
			if(key[i][j] == b):
				bi = i
				bj = j
	send = ""
	if(ai==bi):
		send = key[ai][(aj-1)%6] + key[bi][(bj-1)%6]
	elif(aj==bj):
		send = key[(ai-1)%6][aj] + key[(bi-1)%6][bj]
	else:
		send = key[ai][bj] + key[bi][aj]
	return send

print("encrypt or decrypt")
a = raw_input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
	for i in old:
		i=i.lower()
		if(i in alphabet):
			new += i
	old = new
	new = ""
	print(old)
	l = len(old)-1
	i=0
	while(i<l+1):
		a = old[i]
		if(i==l):
			b = "z"
			i += 1
		else:
			b = old[i+1]
			if(a==b):
				b = "x"
				i += 1
			else:
				i += 2
		new += transform(a,b,key_tab)
		
	(open("sample_change.txt", 'w')).write(new)
	
elif(a=="decrypt"):
	old = (open("sample_change.txt")).read()
	new = ""
	l = len(old)-1
	i=0
	while(i<l+1):
		a = old[i]
		b = old[i+1]
		new += reform(a,b,key_tab)
		i += 2
		(open("sample_returns.txt", 'w')).write(new)
