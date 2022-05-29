#          1 
#        1 2
#      1 2 3
#    1 2 3 4
#  1 2 3 4 5
num=int(input("enter number"))
i=0
while i<=num:
    k=num-i
    while k>0:
        print(" ",end=" ")
        k=k-1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i+1
    print()