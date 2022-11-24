import math
n=int(input("Enter the no of cuts:"))
x=360
if 2<=n<=36:
    if n%x==0:
        ans=x//n
        print()
        print("Cake can be divided int0",ans,"equal parts")
    else:
        ans=x//n
        ans2=x-(ans*n)
        print()
        print("Cake can be divided into equal parts of",ans,"degree and one small part of",ans2,"degree")
else:
    print("It's not possible to cut the cake")

from turtle import*
circle(100)
pensize(10)
color("blue")
circle(100,ans)
input()