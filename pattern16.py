# 1
# 1 2
# 1 3 4
# 1 5 6 7
a=int(input("enter number"))
i=1
sum=1
while i<a:
    j=1
    while j<=i:
        
        if j==1:
            print(j,end=" ")
        else:
            sum=sum+1
            print(sum,end=" ")
        j=j+1
    print()
    i=i+1