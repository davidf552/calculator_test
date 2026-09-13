print("Welcome to the python calculator!")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print("Numbers entered are:", num1, "and", num2)

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input())

if operation == 1:
    result = num1 + num2
    print("The result of addition is:", result)