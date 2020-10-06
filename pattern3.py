n=int(input())
c=0
z=n
while z>0:
	if z%2!=0 :
		z=z-2
		c=c+1
for i in range(n-c+1):
	for j in range(n):
		if j>=n-c-i and j<=n-c+i :
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
input()