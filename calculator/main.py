
from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add ,
    "-": subtract ,
    "*": multiply,
    "/": divide,
}

def calulator():
    print (logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operators:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calulator()

calulator()

