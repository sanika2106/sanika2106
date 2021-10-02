# Write a program to display all even numbers that fall between two numbers (exclusive both numbers) 
# entered by the user.
num=int(input("enter the number:"))
num2=int(input("enter the number:"))
# i=num
i=num
while i<num2:
    if i%2==0:
     print(i,"even number")
    else:
     print(i,"odd number")
    i+=1 
    