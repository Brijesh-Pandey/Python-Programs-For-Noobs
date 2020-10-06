num=input()
count=0

def count_zeroes(num,count,si):

    if len(num)==0 or si==len(num):
       # print("base case")
        return 0
    if num[si]=='0':
        #print("hi")
        count+=1
    sum=0+count
    if si==len(num)-1:
        print(sum)
    s= count_zeroes(num, count, si + 1)
   # return 0+count


count_zeroes(num,count,0)
