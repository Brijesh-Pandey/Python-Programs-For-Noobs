import itertools
li=[1,0,-1,-2,2,0]
li2=[]
sum=0
print(li)
sq=list(itertools.combinations(li,4))
for i in sq:
    sum=0
    for j in i:
        sum=sum+j

    if sum==0:
        li2.append(i)
print(li2)