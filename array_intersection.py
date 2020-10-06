def array_intersection(li,li2):
	li3=[]
	for i in range(n):
		for j in range(n):
			if li[i]==li2[j]:
				li3.append(li2[j])
	return li3

n=int(input())
li=[int(x) for x in input().split()]
li2=[int(x) for x in input().split()]
x=array_intersection(li,li2)
print(x)
