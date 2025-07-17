def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: 0으로 나눌 수 없습니다."
    return a / b

def main():
    try:
<<<<<<< HEAD
        a = int(input("첫 번째 숫자를 입력하세요 : "))
        b = int(input("두 번째 숫자를 입력하세요 : "))
=======
        a = float(input("첫 번째 숫자를 입력하세요 : "))
        b = float(input("두 번째 숫자를 입력하세요 : "))
>>>>>>> a23dd09 (ia)
    except ValueError:
        print("잘못된 숫자 입력입니다.")
        return
    
    operator = input("연산자를 입력하세요 (+, -, *, /): ")

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        print("잘못된 연산자입니다.")
        return

    print(f"결과: {result}")

if __name__ == "__main__":
    main()