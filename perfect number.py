#21MCA031
#MATHU S KULATHUMKAL

num=int(input("Enter the number: "))
sum_a=0
for i in range(1,num):
    if (num%i==0):
        sum_a=sum_a+i
if(sum_a==num):
    print("The entered number is a perfect number")
else:
    print("The entered number is not a perfect number")