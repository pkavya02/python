import sys

def add(num1,num2):
    a = num1 + num2
    return a

def sub(num1,num2):
    s = num1 - num2
    return s

def mul(num1,num2):
    m = num1 * num2
    return m 

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    res = add(num1,num2)
    print(res)
elif operation == "sub":
    res = sub(num1,num2)
    print(res)
elif operation == "mul":
    res = mul(num1,num2)
    print(res)
else:
    print("unknow operation")
          

 