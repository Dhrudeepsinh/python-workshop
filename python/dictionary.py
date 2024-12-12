n1={}

n=int(input("Enter num of element:"))

for i in range(0,n):
    a,b=input("Enter key value pair data:").split()
    n1[a]=[b]
print(n1)