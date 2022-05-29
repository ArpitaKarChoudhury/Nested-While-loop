#        1 
#      2 1
#    3 2 1
#  4 3 2 1
#5 4 3 2 1
num=int(input("enter number"))
i=1
while i<=num:
    k=num-i
    while k>0:
        print(" ",end=" ")
        k=k-1
    j=0
    while j<i:
        print(i-j,end=" ")
        j=j+1
    i=i+1
    print()