# print following series till n term 
# 1 , 4 , 9 , 16 , 25 ,.....n term



n=int(input("enter number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j**2,end=" ")
        j+=1
    print( )
    i+=1