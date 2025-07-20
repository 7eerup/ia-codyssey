def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

OPERATORS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

OP_PRIORITY = [["*", "/"], ["+", "-"]]  # 연산자 우선순위

def calculate(tokens, ops):
    idx = 0
    while idx < len(tokens):
        op = tokens[idx]
        if op in ops:
            try:
                left = float(tokens[idx - 1])
                right = float(tokens[idx + 1])
                result = OPERATORS[op](left, right)
            except (ValueError, IndexError):
                return "Invalid input."

            if isinstance(result, str):  # divide 함수 에러 메시지
                return result

            tokens[idx - 1:idx + 2] = [str(result)]
            idx = max(idx - 1, 0)
        else:
            idx += 1
    return tokens

def is_valid(tokens):
    if len(tokens) < 3 or len(tokens) % 2 == 0:
        return False
    for i, token in enumerate(tokens):
        if i % 2 == 0:  # 숫자 위치
            try:
                float(token)
            except ValueError:
                return False
        else:  # 연산자 위치
            if token not in OPERATORS:
                return False
    return True

def main():
    number = input("계산식을 입력하세요 (예: 4 + 5 * 3 - 2): ")
    tokens = number.split()

    if not is_valid(tokens):
        print("Invalid input.")
        return

    for ops in OP_PRIORITY:
        tokens = calculate(tokens, ops)
        if isinstance(tokens, str):
            print(tokens)
            return

    print(f"Result: {float(tokens[0])}")

if __name__ == "__main__":
    main()
