#! /usr/bin/python2
import time

start_time=time.time()
n1=1
n2=2
sum = n2

'''time taken=3.71932983398e-05'''
#while n2<=4000000:
#	n1,n2=n2,n1+n2 
#	if n2% 2 == 0:
#		sum=sum+n2

'''time taken=3.19480895996e-05'''
while n2<=4000000:
	n1,n2=n2,n1+n2 #odd
	n1,n2=n2,n1+n2 #odd
	n1,n2=n2,n1+n2 #even    
	sum=sum+n2

sum=sum-n2
print sum
print time.time() - start_time
