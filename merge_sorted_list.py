def merge_sorted(li1, li2, n, m):
    i = 0
    j = 0
    li3 = []
    while i < n and j < m:
        if li1[i] > li2[j]:
            li3.append(li2[j])
            j = j + 1
        else:
            li3.append(li1[i])
            i = i + 1
    while i < n:
        li3.append(li1[i])
        i = i + 1
    while j < m:
        li3.append(li2[j])
        j = j + 1
    for i in li3:
        print(i,end=" ")

n=int(input())
m=int(input())
li1 = [int(x) for x in input().split()]
li2 = [int(y) for y in input().split()]
merge_sorted(li1, li2, n, m)
