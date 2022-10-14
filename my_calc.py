def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero")

def ascend_descend(length, minimum, maximum):
    string = ""
    for i in range(minimum, length + 1):
        string += str(i)
        if i == maximum:
            new = string[:-1]
            string += new[::-1]
            break
    print(string)

ascend_descend(5, 1, 3)




