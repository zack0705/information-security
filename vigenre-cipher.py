print("encrypt or decrypt")
a = input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	k = input("enter key")
	j=0
	for i in old:
		new += chr((ord(i)+ord(k[j]))%256)
		j+=1
		if(j==len(k)):
			j=0
	(open("sample_change.txt", 'w')).write(new)	
	

if(a=="decrypt"):
	old = (open("sample_change.txt")).read()
	new = ""
	k = input("enter key")
	j=0
	for i in old:
		new += chr((ord(i)-ord(k[j]))%256)
		j+=1
		if(j==len(k)):
			j=0
	(open("sample_returns.txt", 'w')).write(new)	
	
