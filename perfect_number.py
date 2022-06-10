# 6=6*1
# 6=1*6 
# 6=3*2
# 6=2*3 
# 6=1+2+3
from re import I


a=int(input("enter number"))
i=1
b=0
while i<=a:
    if a%i==0 and a>i:
        c=a//i
        d=c*i
        b=b+i
    i=i+1
if a==b and a==d:
    print(a,"is perfect number")
else:
    print(a,"is not A perfect number")