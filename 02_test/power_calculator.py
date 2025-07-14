def main():
    try:
        number_input = input("숫자를 입력하세요: ")
        base = float(number_input)

    except ValueError:
        print("잘못된 숫자 입력입니다.")
        return
    
    try:
        power_input = input("몇 제곱을 할까요? (정수로 입력): ")
        power = int(power_input)

    except ValueError:
        print("제곱 수는 정수로 입력해야 합니다.")
        return
    
    result = 1.0
    
    for _ in range(abs(power)):
        result *= base

    if power < 0:
        result = 1 / result

    print(f"결과: {int(result) if result.is_integer() else result}")

if __name__ == "__main__":
    main()
