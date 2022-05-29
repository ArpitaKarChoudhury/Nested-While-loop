# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
i=0
num=int(input("enter number"))
while i<=num:
    j=1
    while j<=num-i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1