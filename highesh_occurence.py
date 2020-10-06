str=input()
highest=0
j=1
li=list(str)
print(li)
for i in range(len(li)):
    count=li.count(li[i])
    for j in range(len(li)):
        if count>li.count(li[j]):
            highest=li[i]
        else:
            highest=li[j]
            count=li.count(li[j])
        print(highest,end=" ")
    print()
#print(highest)