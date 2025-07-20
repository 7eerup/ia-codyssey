def bubble_sort(numbers):
    
    n = len(numbers)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def main():
    try:
        # 사용자 입력 받고 공백 기준으로 분리
        input_str = input("숫자들을 공백으로 입력하세요: ")

        # 입력이 비어 있으면 예외 처리
        if not input_str:
            print("Invalid input.")
            return

        # 숫자 문자열을 float으로 변환
        number_list = [float(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input.")
        return

    # 버블 정렬 알고리즘으로 정렬
    sorted_list = bubble_sort(number_list)

    # 출력 (소수점 유지)
    print(f"Sorted:, {sorted_list}")

if __name__ == "__main__":
    main()


