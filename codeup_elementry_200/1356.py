n = int(input())

for i in range(n):
    if i == 0:
        print("*"*n)
    elif i == n-1:
        print("*"*n)
    else:
        print("*"," "*(n-2),"*",sep="")