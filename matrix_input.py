n=int(input())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
#z=len(li[0])
#print(z)

for i in li:
    for j in i:
        print(j,end=" ")
    print()