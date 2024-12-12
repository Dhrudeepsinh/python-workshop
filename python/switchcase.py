print("Enter No1:")
a=input()
print("Enter No2:")
b=input()
c=int(a)+int(b)
print(c)

def one():
    return "c is 30"

def two():
    return "C is greter 30"

def three():
    return "C is less 30"

switcher = {
    1: one,
    2: two,
    3: three
}
print(type(switcher))
value = 2
result = switcher.get(value, lambda: "unknown")()
print(result)
