n=int(input())
li=list(int(x) for x in input().split())
k=int(input())
#APPROACH-1
'''
def isPresent(a,k):
    l=len(a)
    if l==0:
        return
    if a[0]==k:
        #print("From this")
        return True
    small=a[1:]
    if isPresent(small,k):
        #print("from 2")
        return True
    else:
        return False
print(isPresent(li,k))
'''

#Approach-2

def isPresent2(a,k,si):
    if len(a)==0 or si==len(a):
        return
    if a[si]==k:
        print("From this")
        return True
    if isPresent2(a,k,si+1):
        return True
    else:
        return False

print(isPresent2(li,k,0,))