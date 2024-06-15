def calculator():
    num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operation = input("Choose the operation (+, -, *, /): ")
        if operation == '+':
        result = num1 + num2
        print("The result is:", result)
    elif operation == '-':
        result = num1 - num2
        print("The result is:", result)
    elif operation == '*':
        result = num1 * num2
        print("The result is:", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("The result is:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
calculator()

/*OUTPUT

Enter the first number: 1
Enter the second number: 5
Choose the operation (+, -, *, /): +
The result is: 6.0*/
