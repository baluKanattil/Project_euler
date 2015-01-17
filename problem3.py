#! /usr/bin/python2

#only check for odd factors.

max_factor=1
i=3
n=600851475143

while n!=1:
	while n%i==0:
		n=n/i
		max_factor=i
	i=i+2

print max_factor
