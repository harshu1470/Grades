#!/usr/bin/pyhton36

l=[0,1]
N= int(input("enter the number till there you want to print fibonacci series"))
n3=0
for i in range(N-2):
	l1= l[i] +l[i+1]
	l.append(l1)
	
print(l)

	
