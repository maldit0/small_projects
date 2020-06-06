print("Enter two numbers. I'll divide them.")
x = input("First number: ")
y = input("Second number: ")
try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(result)