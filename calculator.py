operation_num1 = int(input("Enter number 1: "))
operand = input("Enter operand: ")
operation_num2 = int(input("Enter number 2: "))

def arithematic(operation_num1, operand, operantion_num2):
    if operand == "+":
        answer = operation_num1 + operantion_num2
    elif operand == "-":
        answer = operation_num1 - operantion_num2
    elif operand == "*":
        answer = operation_num1 * operation_num2
    elif operand == "/":
        answer = operation_num1 / operantion_num2
    else:
        print("Invalid Operation")
    return answer     

print(arithematic(operation_num1, operand, operation_num2))


  
