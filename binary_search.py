"""Binary Search"""
def binary_search(li,item):
	start =0
	end=len(li)-1
	while start<=end:
		mid= start + end //2
		if li[mid] == item:
			return mid
			break
		elif item<li[mid]:
			end=mid-1
		elif item>li[mid]:
			start=mid+1
	return -1

li=[int(x) for x in input().split()]
item=int(input("Item to be Searched "))
z=binary_search(li,item)
print(z)
input()