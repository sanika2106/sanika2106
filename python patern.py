# name patern printing


string=input("enter the string:")
i=0
while i<len(string):
    j=0
    while j<=i:
        print(string[i],end=" ")
        j+=1
    i+=1
    print( )
    
