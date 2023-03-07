oper = input("Enter operation using an appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")
x = input("Enter first component: ")
y = input("Enter second component: ")
if oper == '1':
    print("Adding ", float(x), "and", float(y))
    print("Result: ", float(x) + float(y))
elif oper == '2':
    print("Subtracting ", float(x), "and", float(y))
    print("Result: ", float(x) - float(y))
elif oper == '3':
    print("Multiplicating ", float(x), "and", float(y))
    print("Result: ", float(x) * float(y))
elif oper == '4':
    print("Dividing ", float(x), "and", float(y))
    print("Result: ", float(x) / float(y))