def isunique(li):
	for i in range(n):
		if li.count(li[i])%2 != 0:
			print(li[i])

n=int(input())
li=[int(x) for x in input().split()]
isunique(li)
input()