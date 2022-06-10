# 1
# 1 2
# 1 4 3
# 1 6 9 4
a=int(input("enter number"))
i=1
sum=1
while i<=a:
    j=1
    while j<=i:
        
        if j==1:
            print(j,end=" ")
        elif i==j:
            print(i,end=" ")
        else:
            print(j*(i-1),end=" ")
        j=j+1
    print()
    i=i+1