print("encrypt or decrypt")
a = input()

if(a=="encrypt"):
	old = (open("sample.txt")).read()
	new = ""
	k=int(input("enter key"))
	n = len(old)
	i=0
	l=[]
	for j in old:
		l.append(j)
	l=l[:-1]
	n-=1
	i=0
	j=0
	while(1):
		z = (2*i*k)-(2*i)
		if(z>n):
			break
		new += l[z]
		i+=1
	i=0
	j=1
	while(1):
		y = (2*i*k)-(2*i)-j
		z = (2*i*k)-(2*i)+j
		if(z==k-1):
			break
		if(y>0 and y<n):
			new+=l[y]
		if(z<n):
			new+=l[z]
			i+=1
		if(z>=n):
			i=0
			j+=1
	i=0
	while(1):
		z = (2*i+1)*k-(2*i+1)
		if(z>=n):
			break
		else:
			new+=l[z]
			i+=1
			
	(open("sample_change.txt", 'w')).write(new)
	
elif(a=="decrypt"):

	a = input("normal or brute")	
	
	old = (open("sample_change.txt")).read()
	new = ""
	i=0
	j=0
	l=[]
	p=0
	n = len(old)
	
	for i in range(len(old)):
		l.append("_")
	i=0
	
	if(a=="normal"):
	
		k = int(input("enter key"))
		while(1):
			z = 2*i*k-2*i
			if(z>n):
				break
			l[z] = old[p]
			p+=1
			i+=1

		i=0
		j=1
	
		while(1):
			y = (2*i*k)-(2*i)-j
			z = (2*i*k)-(2*i)+j
			if(z==k-1):
				break
			if(y>0 and y<n):
				l[y] = old[p]
				p+=1
			if(z<n):
				l[z] = old[p]
				i+=1
				p+=1
			if(z>=n):
				i=0
				j+=1

		i=0
		while(1):
			z = (2*i+1)*k-(2*i+1)
			if(z>=n):
				break
			else:
				l[z]=old[p]
				i+=1
				p+=1
		new=""
		for i in l:
			new+=i
		(open("sample_returns.txt", 'w')).write(new)

	elif(a=="brute"):
		po = ""
		k=1
		while(po!="ok"):
			k+=1
			i=0
			p=0	
			i=0
			while(1):
				z = 2*i*k-2*i
				if(z>=n):
					break
				l[z] = old[p]
				p+=1
				i+=1

			i=0
			j=1
	
			while(1):
				y = (2*i*k)-(2*i)-j
				z = (2*i*k)-(2*i)+j
				if(z==k-1):
					break
				if(y>0 and y<n):
					l[y] = old[p]
					p+=1
				if(z<n):
					l[z] = old[p]
					i+=1
					p+=1
				if(z>=n):
					i=0
					j+=1

			i=0
			while(1):
				z = (2*i+1)*k-(2*i+1)
				if(z>=n):
					break
				else:
					l[z]=old[p]
					i+=1
					p+=1
			new=""
			for i in l:
				new+=i
				
			print(new)
			
			po = input("is it ok?")
			(open("sample_returns.txt", 'w')).write(new)

