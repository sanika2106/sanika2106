
# prime number

num=int(input("enter the number:"))
i=num 
while i<=num:
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print("prime number",i)
    elif i==2 or i==3 or i==5 or i==7:
        print("prime number",i)
    else:
        print("not prime number",i)
    i+=1 

