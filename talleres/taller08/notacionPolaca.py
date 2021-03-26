from collections import deque
def polaca(operation):
    stack = deque()
    operators = "+*/-%"      
    for i in range(0, len(operation)):
        if operation[i]== " ":
            continue
        if operation[i] in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            operator = operation[i]
            if operator == "+":
                stack.append(num2+num1)
            elif operator == "-":
                stack.append(num2-num1)
            elif operator == "*":
                stack.append(num2*num1)
            elif operator == "/":
                stack.append(num2/num1)
            elif operator == "%":
                stack.append(num2%num1)
        else:
            stack.append(int(operation[i]))
    return stack.pop()

print(polaca("3 5 * 2 +"))
print(polaca("6 5 - 4 +"))