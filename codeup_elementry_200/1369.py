n,k = map(int,input().split())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end="")
        elif (i+j+1)%k==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()