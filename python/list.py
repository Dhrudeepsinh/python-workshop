list=[]

n=int(input("enter num of element:"))

for i in range(0,n):
    a = int(input("enter num:"))
    a=a*3
    list.append(a)
print(list)

for i in range(0,len(list)):
    for i in range(len(list)-1):
            if (list[i]>list[i+1]):
                list[i],list[i+1]=list[i+1],list[i]
print("Aescending",list)

for i in range(0,len(list)):
    for i in range(len(list)-1):
        if (list[i]<list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]
print("Descending",list)