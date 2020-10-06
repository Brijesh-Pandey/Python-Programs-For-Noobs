def harshad_number(num):
    original_number=num
    sum = 0
    if num==0:
        pass

    else:
        while num>0:
            rem=num%10
            sum=sum+rem
            num=num//10
        if original_number%sum==0:
            print(original_number)
for i in range(101):
    harshad_number(i)