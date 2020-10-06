## Read input as specified in the question.
## Print output as specified in the question.
def shiftedNumber(li):
    for i in range(n-1):
        if li[i]>li[i+1]:
            return i+1
    return 0
n=int(input())
li=[int(x) for x in input().split()]
z=shiftedNumber(li)
print(z)