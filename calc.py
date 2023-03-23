# calculator
import logging
logging.basicConfig(level=logging.DEBUG)
oper = input("Enter operation using an appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")
x = input("Enter first component: ")
y = input("Enter second component: ")

# finally get where to use logging ;)
if oper == '1':
    a = input("Enter one more component or 0: ")
    logging.info(f"Adding {float(x)} and {float(y)} and {float(a)}")
    print("Result: ", float(x) + float(y) + float(a))
elif oper == '2':
    logging.info(f"Subtracting {float(x)} and {float(y)}")
    print("Result: ", float(x) - float(y))
elif oper == '3':
    m = input("Enter one more component or 1: ")
    logging.info(f"Multiplicating {float(x)} and {float(y)} and {float(m)}")
    print("Result: ", float(x) * float(y) * float(m))
elif oper == '4':
    logging.info(f"Dividing {float(x)} and {float(y)}")
    print("Result: ", float(x) / float(y))
