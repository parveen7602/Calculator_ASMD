import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multliply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict = {
    '+': add,
    '-': subtract,
    '*': multliply,
    '/': divide
}
def calculate():
    number1 = float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("Enter second number: "))
        calculator_function=operations_dict[operation_symbol]
        output=calculator_function(number1, number2)
        print(f"{number1} {operation_symbol} {number2}={output}")
        should_continue=input("Enter 'y' to continue calculation with output or 'n' to start a new calculation or 'x' to exit: ")
        if should_continue == 'y':
           number1 = output
        elif should_continue == 'n':
           continue_flag=False
           os.system('cls')
           calculate()
        else:
           continue_flag=False
           print("Thank you for using this calculator! Have a nice day! Bye!..")
calculate()