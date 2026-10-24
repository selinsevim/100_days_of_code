import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation_dict = {"+":add, "-":subtract, "*":multiply, "/":divide}

#print(operation_dict["*"](4,8))

def operation(first_number, second_number, math_operation):
    output_opt= float(operation_dict[math_operation](first_number, second_number))
    print(f"Result is output: {output_opt}")
    return output_opt

while True:
    first = float(input("Type the first number\n"))
    while True:
        math_opt = input("Type a mathematical operator (a choice of +, -, * or /)\n")
        second = float(input("Type the second number\n"))
        output = operation(first, second, math_opt)
        print(output)
        answer = input("Do you want to continue from the previous result? Type yes or no\n")

        if answer == "no":
            break
        else:
            first = output