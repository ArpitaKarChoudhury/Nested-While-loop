# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
i=1
num=int(input("enter number"))
while i<=num:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1