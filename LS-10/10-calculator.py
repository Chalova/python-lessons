from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    want_continue = True

    while want_continue:
        user_operator = input("Select any of operators:")
        num2 = float(input("What is the next number? "))
        culc_function = operations[user_operator]
        answer = culc_function(num1, num2)
        print(f"{num1} {user_operator} {num2} = {answer}")
        to_continue = input("Do you want to continue? Type [yes] or type [no] to start over again")
        if to_continue == "no":
            want_continue = False
            calculator()
        else:
            num1 = answer

calculator()

