import urllib.request as uuuu

def transform(a,key):
	b = (a+key)%256
	return b

def reform(b,key):
	a = (b-key)%256
	return(a)

print("encrypt or decrypt")
a = input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	key=int(input("enter key"))
	for i in old:
		a = ord(i)
		b = chr(transform(a,key))
		new += b

	(open("sample_change.txt", 'w')).write(new)

elif(a=="decrypt"):
	print("normal or brute or freq")
	a = input()
	old = (open("sample_change.txt")).read()
	new = ""
	if(a=="normal"):
		for i in old:
			a = ord(i)
			key = int(input("enter key"))
			b = chr(reform(a,key))
			new += b

		(open("sample_returns.txt", 'w')).write(new)

	elif(a=="brute"):
		key = 0
		while(a!="ok"):
			new = ""
			print("key = "+str(key)+"---------------------------------------------------------------------")
			for i in old:
				a = ord(i)
				b = chr(reform(a,key))
				new += b
			print(new)
			print("is it ok?")
			a = input()	
			key+=1
		(open("sample_returns.txt", 'w')).write(new)
	
	elif(a=="freq"):
		D = {}
		internet = " etaoinsrhdlucmfywgpbvkxqjz0123456789"
		for i in old:
			try:
				D[i] = D[i]+1
			except:
				D[i] = 1
		maxn = 0
		maxc = ""
		for i in D:
			if(D[i]>maxn):
				maxn = D[i]
				maxc = i
		print("max is = "+str(maxc)+"-------------------------------------------------")
		
		for i in internet:
			a = ord(i)
			b = ord(maxc)
			key = (b-a)%256
			print("key = " +str(key)+"------------------------------------------------------------------")
			new = ""
			for j in old:
				a = ord(j)
				b = chr(reform(a,key))
				new += b
			print(new)
			print("is it ok")
			z = input()
			if(z=="ok"):
				print("key = "+str(key))
				break
