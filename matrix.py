li=[[21,12,31],[54,45,66],[7,8,9]]
k=2
for i in range(3-k+1):
    for j in range(3-k+1):
        for p in range(i,k+i):
            for q in range(j,k+j):
                print(li[p][q],end=" ")
            print()

        print()