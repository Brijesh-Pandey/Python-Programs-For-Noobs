''' APPROACH-1
Jewels=input()
Stone=input()
count=0
for i in Jewels:
    for j in Stone:
        if i==j:
            count=count+1
        else:
            pass
print(count)
'''
''' APPROACH -2'''
Jewels=input().strip('"')
Stone=input().strip('"')
output=0
for i in list(Jewels):
    z=(list(Stone)).count(i)
    output+=z
print(output)
