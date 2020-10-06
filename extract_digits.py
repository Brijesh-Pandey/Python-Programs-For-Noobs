str=input()
list(str)
li=[]
li2=[]
size=len(str)
for i in range(size):
    if str[i]>='0' and str[i]<='9':
        li.append(str[i])
        flag=0
    if str[0]=='-':
        if str[i]>='0' and str[i]<='9':
            flag=1
            li2.append(str[i])
if flag==0:
    print("".join(li))

else:
    print("-",end="")
    print("".join(li))