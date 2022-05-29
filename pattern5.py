# 5 4 3 2 1
# 5 4 3 2 
# 5 4 3
# 5 4
# 5
i=1
num=int(input("enter number"))
while i<=num:
    j=0
    while j<=num-i:
        print(num-j,end=" ")
        j=j+1
    print()
    i=i+1