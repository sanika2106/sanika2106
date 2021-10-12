
# Write a program to accept 10 numbers from the user and display it’s average.
# num=int(input("enterthe number:"))
i=1
sum=0
while i<=10:
   num=int(input("enter the number:"))
   sum+=num
   i+=1
print(sum,"average=",num/sum*100)


