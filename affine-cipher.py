import sys

def inv(a,b):
	a = a%b
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
		
	x = (a*t1)%b
	if(x==1):
		print(t1%256)
		return(t1%256)
	else:
		return(-1)

	print("r1 = "+str(r1))

def transform(a,km,ka):
	b = ((a+ka)*km)%256
	return b
	
def reform(a,km,ka):
	b = ((a*km)-ka)%256
	return b

print("encrypt or decrypt")
a = input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	key_mul = int(input("enter mul key"))
	key_add = int(input("enter add key"))

	if(inv(key_mul,256)==-1):
		print("invalid")
		sys.exit()
	
	for i in old:
		a = ord(i)
		b = chr(transform(a,key_mul,key_add))
		new += b

	(open("sample_change.txt", 'w')).write(new)	
	
elif(a=="decrypt"):
	old = (open("sample_change.txt")).read()
	new = ""
	key_mul = int(input("enter mul key"))
	key_add = int(input("enter add key"))

	if(inv(key_mul,256)==-1):
		print("invalid")
		sys.exit()

	key_mul = inv(key_mul,256)

	for i in old:
		a = ord(i)
		b = chr(int(reform(a,key_mul,key_add)))
		new += b
		
	(open("sample_returns.txt", 'w')).write(new)
