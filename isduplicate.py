def isduplicate(li):
	for i in range(n):
		if li.count(li[i])>=2:
			print(li[i])
			break
n=int(input())
li=[int(x) for x in input().split()]
isduplicate(li)
input()