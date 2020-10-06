k=0
for i in range(4):
	p=k+1
	for j in range(i+1):
			if i%2==0:				
				print(p, end=" ")
				p+1
				
			else :				
				print(k, end=" ")
				p-1
				
	print()
input()