
# prime number

i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0:
        print("prime number",i)
    elif i==2 or i==3 or i==5:
        print("prime number",i)
    else:
        print("not prime number",i)
    i+=1 