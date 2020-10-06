d=1
for i in range(5,-1,-1):
	k=1
	c=d
	for j in range(0,11,1):
		if j>=5-i and j<=5+i and k:
			print(d,end="")
			d=d+1
			k=0
		else:
			print(" ",end="")
			k=1
	d=c+1
	print()

for i in range(5):
	k=1
	for j in range(0,11,1):
		if j>=4-i and j<=6+i and k:
			print("*",end="")
			k=0
		else:
			k=1
			print(" ",end="")
	print()
input()