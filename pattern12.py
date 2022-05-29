# 5
# 5 4
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1
i=0
num=int(input("enter number"))
while i<num:
    j=0
    while j<=i:
        print(num-j,end=" ")
        j=j+1
    print()
    i=i+1