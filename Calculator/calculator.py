import operator

program_name='''
   _____      _            _       _
  / ____|    | |          | |     | |
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
  '''

def calculator():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }

    print("Welcome to my", program_name)
    print("\nProject Name: Calculator in Python")
    print("Intern Name: Rethar Osman Abdullah")
    print("Intern ID: CC36307")
    print("Designation: Python Development Intern\n")
    print("\nPlease select an operator from the following options:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("** : Exponentiation")
    print("% : Modulus (Remainder)")
    print("// : Floor Division (Rounded down)")

    while True:
        operator_symbol = input("\nEnter the operator symbol: ")
        if operator_symbol not in operators:
            print("\nInvalid operator")
            continue

        num1 = None
        while num1 is None:
            try:
                num1 = float(input("\nEnter the first number: "))
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        num2 = None
        while num2 is None:
            try:
                num2 = float(input("\nEnter the second number: "))
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        operation = operators[operator_symbol]
        result = operation(num1, num2)
        print("\nResult:", result)

        while True:
            choice = input("\nDo you want to calculate more? (y/n): ")
            if choice.lower() == 'n':
                print("\nThank you for using the Calculator Program!")
                return
            elif choice.lower() == 'y':
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

calculator()
