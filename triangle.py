a= int(input("enter number"))
i=1
while i<=a:
    c=a
    while c>=1:
        print(" ",end=" ")
        c=c-1
    d=1
    while d<=i:
        if i==d:
            print("*",end=" ")
        else:
            print(" ",end="")
        d=d+1
    print()
    i=i+1
