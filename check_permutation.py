def check_permutation(str1,str2):
	sum1,sum2,i=0,0,0
	if len(str1)==len(str2):
		for i in range(len(str1)):
			sum1+=ord(str1[i])
		for i in range(len(str2)):
			sum2+=ord(str2[i])
		if sum2==sum1:
			return True
		else:
			return False
	else:
		return False
str1=input()
str2=input()
z=check_permutation(str1,str2)
print(z)