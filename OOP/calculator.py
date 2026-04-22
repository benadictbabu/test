a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = input("Enter your choice (1/2/3/4/5): ")
if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b) 
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == '5':
    print("Exiting the calculator.")
else:
    print("Invalid choice. Please enter a valid option.")
