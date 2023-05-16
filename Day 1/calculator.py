def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("Enter Two Numbers: ", end="")
nOne = int(input())
nTwo = int(input())
print("Enter the Operator (+, -, *, /): ", end="")
ch = input()

if ch == '+':
    print("\n" + str(nOne) + " + " + str(nTwo) + " = " + str(add(nOne, nTwo)))
elif ch == '-':
    print("\n" + str(nOne) + " - " + str(nTwo) + " = " + str(sub(nOne, nTwo)))
elif ch == '*':
    print("\n" + str(nOne) + " * " + str(nTwo) + " = " + str(mul(nOne, nTwo)))
elif ch == '/':
    print("\n" + str(nOne) + " / " + str(nTwo) + " = " + str(div(nOne, nTwo)))
else:
    print("\nInvalid Operator!")
