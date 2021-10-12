#leap year

i=2002
while i<=2020:
    if i%4==0:
        print("leap year",i)
    elif i%400==0:
        print("also leap year",i)
    else:
        print("not leap year",i)
    i+=1