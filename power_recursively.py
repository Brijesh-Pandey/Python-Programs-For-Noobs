n=int(input())
x=int(input())
def power_rec(num,pow):
    if pow==0:
        return 1
    smalloutput=power_rec(num,pow-1)
    return smalloutput*num
print(power_rec(n,x))