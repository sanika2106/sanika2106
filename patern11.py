#         *
#       * *
#     * * *
#   * * * *
# * * * * *


i=1
while i<=5:
    a=1
    while a<=5-i:
        print(" ",end=" ")
        a+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print( )
    i+=1