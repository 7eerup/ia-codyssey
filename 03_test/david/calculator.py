def add(a, b):
    return (a, b)

def subtract(a, b):
    return (a, b)

def multiply(a, b):
    return (a, b)

def divide(a, b):
    if b == 0:
        return "Error Division by zero."
    return a

if __name__ == "__main__":
    try:
        a = int(float(input("첫 번째 숫자를 입력하세요 : ")))
        b = int(float(input("두 번째 숫자를 입력하세요 : ")))

        operator = input("연산자를 입력하세요 + - * /")
        
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator"

        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. 숫자를 올바르게 입력해주세요.")