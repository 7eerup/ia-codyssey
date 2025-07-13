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

def calculate_expression(expr):
    try:
        parts = expr.strip().split()
        if len(parts) != 3:
            return "잘못된 수식 형식입니다. 예: 2 + 3"

        a, operator, b = parts
        a = float(a)
        b = float(b)

        if operator == "+":
            return add(a, b)
        elif operator == "-":
            return subtract(a, b)
        elif operator == "*":
            return multiply(a, b)
        elif operator == "/":
            return divide(a, b)
        else:
            return "허용되지 않은 연산자입니다."

    except ValueError:
        return "숫자 입력이 잘못되었습니다."
    except Exception as e:
        return f"오류 발생: {e}"

def main():
    mode = input("모드 선택: (1) 숫자와 연산자 따로 입력, (2) 한 줄 수식 입력 : ")

    if mode == "1":
        try:
            a = int(input("첫 번째 숫자를 입력하세요 : "))
            b = int(input("두 번째 숫자를 입력하세요 : "))
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

    elif mode == "2":
        expr = input("수식을 입력하세요 (예: 2 + 3): ")
        result = calculate_expression(expr)
        print(f"결과: {result}")

    else:
        print("잘못된 모드 선택입니다.")

if __name__ == "__main__":
    main()
