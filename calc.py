oper = input("Enter operation using an appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")
first_component = input("Enter first component: ")
second_component = input("Enter second component: ")
if oper == '1':
    print("Adding ", float(first_component), "and", float(second_component))
    print("Result: ", float(first_component) + float(second_component))
elif oper == '2':
    print("Subtracting ", float(first_component), "and", float(second_component))
    print("Result: ", float(first_component) - float(second_component))
elif oper == '3':
    print("Multiplicating ", float(first_component), "and", float(second_component))
    print("Result: ", float(first_component) * float(second_component))
elif oper == '4':
    print("Dividing ", float(first_component), "and", float(second_component))
    print("Result: ", float(first_component) / float(second_component))