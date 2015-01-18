palin=['1']
nums=[]
for i in range(10,1000):
	for j in range(10,1000):
		num=list(str(i*j))
		flag=1
		n=len(num)
		for k in range(0,n/2):
			flag=flag*(num[k]==num[n-k-1])
		if flag and int(''.join(num))>int(''.join(palin)):
			palin=num
			
		

print palin

