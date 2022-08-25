#21MCA031
#MATHU S KULATHUMKAL

n=int(input("enter the limit:"))
f=0
s=1
t=0
print(f)
print(s)
count=3
while(count<=n):
    t=f+s
    f=s
    s=t
    print(t)
    count=count+1