list=[]

n=int(input("enter num of sub:"))

j=1
for i in range(0,n):
    print("Enter marks of Subject",j,":")
    a = int(input())
    list.append(a)
    j=j+1
print(list)

sum=0
for i in range(0,n):
    sum=sum+list[i]
avg=sum/n
print("Average",avg)

if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")