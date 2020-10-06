m=int(input())
n=int(input())
def multiply(m,n):
    if n==0:
        return 0
    s=multiply(m,n-1)+ m
    return s
print(multiply(m,n))