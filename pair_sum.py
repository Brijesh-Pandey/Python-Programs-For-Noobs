def pair_sum(li):
	for i in range(0,n):
		if li[i]==sum:
				print(li[i],"0")
		for j in range(i+1,n):
			if li[j]==sum-li[i]:
				if li[i]<=li[j]:
					print(li[i],li[j])
				else:
					print(li[j],li[i])
				
n=int(input())
li=[int(x) for x in input().split()]
sum=int(input())
pair_sum(li)
input()
