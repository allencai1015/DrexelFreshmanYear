from stackclass import Stack

def postfix(exp):
    numsStack = Stack()
    chars = exp.split()
    for char in chars:
        if char.isnumeric() or char[1:].isnumeric(): # 2nd statement checks for negative #s
            numsStack.push(int(char))
        elif char == "+" and not (numsStack.isEmpty()):
            x = numsStack.pop()
            y = numsStack.pop()
            z = y + x
            numsStack.push(z)
        elif char == "-" and not (numsStack.isEmpty()):
            x = numsStack.pop()
            y = numsStack.pop()
            z = y - x
            numsStack.push(z)
        elif char == "*" and not (numsStack.isEmpty()):
            x = numsStack.pop()
            y = numsStack.pop()
            z = y * x
            numsStack.push(z)
        elif char == "/" and not (numsStack.isEmpty()):
            x = numsStack.pop()
            y = numsStack.pop()
            z = y / x
            numsStack.push(z)
    return numsStack.pop()

print("Welcome to Postfix Calculator")
print("Enter exit to quit")

expression = input("Enter Expression")
while expression != 'exit':
    result = float(postfix(expression))
    print("Result: {}".format(result))
    expression = input("Enter Expression")