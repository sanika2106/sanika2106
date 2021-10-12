# Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i**3
#     # print(i**3,end=" ""+")
#     print(sum)
#     i+=1



n=int(input("enter number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j**2,end=" ")
        j+=1
    print( )
    i+=1