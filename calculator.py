#simple calculator user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#list of operations
print("choose operators")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. %")

#Get user input for the operation
operation = input("Enter operation number (1,2,3,4,5): ")

#perform calculation based on the operation5
if operation not in ["1","2","3","4","5"]:
    print("Invalid input! Please select a valid operation (1, 2, 3, 4, or 5).")
else:
    if operation == "1":
       results = num1 + num2
       print(f"results = {num1} + {num2} = {results}")
    elif operation == "2":
       results = num1 - num2
       print(f"results = {num1} - {num2} = {results}")
    elif operation == "3":
       results = num1 * num2
       print(f"results = {num1} * {num2} = {results}")
    elif operation == "4":
       if num2 != 0:
          results = num1 / num2
          print(f"result = {num1} / {num2} = {results}")
       else:
          print("Error: Division by zero is not allowed")
    elif operation == "5":
         results = num1 % num2
         print(f"results = {num1} % {num2} = {results}")
    else:
        print("Invalid input! Please select a valid operation (1, 2, 3, or 4).")



