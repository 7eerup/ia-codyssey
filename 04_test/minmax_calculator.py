def main():
    try:
        # 입력 값 받고 기준 분리
        numbers = input("숫자를 공백으로 구분해서 입력하세요.").split()
        # 문자열 float 변환
        float_numbers = [float(num) for num in numbers]
    except ValueError:
        print("잘못된 입력입니다.")
        return
    
    minimum = float_numbers[0]
    maximum = float_numbers[0]

    # 반복문 최소/최대 비교
    for num in float_numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    print(f"최소값: {minimum}, 최대값: {maximum}")

if __name__ == "__main__":
    main()