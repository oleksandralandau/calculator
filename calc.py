oper = input("Enter operation using an appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")
x = input("Enter first component: ")
y = input("Enter second component: ")
if oper == '1':
    a = input("Enter one more component or 0: ")
    print("Adding ", float(x), "and", float(y), "and", float(a))
    print("Result: ", float(x) + float(y) + float(a))
elif oper == '2':
    print("Subtracting ", float(x), "and", float(y))
    print("Result: ", float(x) - float(y))
elif oper == '3':
    m = input("Enter one more component or 1: ")
    print("Multiplicating ", float(x), "and", float(y), "and", float(m))
    print("Result: ", float(x) * float(y) * float(m))
elif oper == '4':
    print("Dividing ", float(x), "and", float(y))
    print("Result: ", float(x) / float(y))