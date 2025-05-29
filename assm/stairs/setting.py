n = int(input())
n1 = n//2
for i in range(1,n1+1):
    for j in range(0,i):
        print('█',end='')
        print(' '*(n1-1), end = '')

    print()


