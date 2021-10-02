# 3 digit armstrong number

n=int(input("enter the 3 digit number number:"))
a=n
sum=0
while n>0:
    b=n%10
    sum=sum+b*b*b
    n=n//10
if sum==a:
    print(a,"is armstrong number")
else:
    print(a,"is not armstrong number")

