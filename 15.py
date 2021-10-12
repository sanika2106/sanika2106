# Prime numbers are those numbers that are divisible by 1 or by themselves. Example:-
# 1.13 is prime because 13 is perfectly divisible by 13 and 1. It is not perfectly divisible by any 
# other number.
# 2.4 is not prime number because 4 is perfectly divisible by 4, 2 and 1.
# For prime numbers you have to check that the number is divisible by how many numbers and you have
#  to use loops also.
# 
    
i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0: 
        print("prime number",i)
    elif i==2 or i==3 or i==5:
        print("it is prime numbers",i)
    else:
        print("it is not prime number",i)
    i+=1
    
