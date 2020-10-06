li=[int(x) for x in input().split()]
def array_revere(li,si):
    if len(li)==0 or si==len(li):
        return 0
    array_revere(li[1:],si+1)
    print(li[0])
array_revere(li,0)