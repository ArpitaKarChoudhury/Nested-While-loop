#        *
#      * *
#    * * *
#  * * * *
#* * * * *
num=int(input("enter number"))
i=0
while i<num:
    k=(num-1)-i
    while k>0:
        print(" ",end=" ")
        k=k-1
    j=i+1
    while j>0:
        print("*",end=" ")
        j=j-1
    i=i+1
    print()