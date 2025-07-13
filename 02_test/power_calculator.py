def main():
    try:
        base_input = input("숫자를 입력하세요: ")
        base = float(base_input)

    except ValueError:
        print("잘못된 숫자 입력입니다.")
        return
    
    try:
        exponent_input = input("지수를 입력하세요: ")
        exponent = int(exponent_input)

    except ValueError:
        print("지수는 정수로 입력해야 합니다.")
        return
    
    result = 1.0
    
    for _ in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1 / result

    print(f"결과: {int(result) if result.is_integer() else result}")

if __name__ == "__main__":
    main()
