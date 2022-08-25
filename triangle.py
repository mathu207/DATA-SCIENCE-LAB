#21MCA031
#MATHU S KULATHUMKAL

a=int(input("enter the side 1:"))
b=int(input("enter the side 2:"))
c=int(input("enter the side 3:"))
if(a==b==c):
    print("equivalent triangle")
elif((a==b!=c)|(a!=b==c)|(a==c!=b)):
    print("issoceless")
else:
    print("scalar")