def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    try:
        # 입력 값 받기 변환
        input_str = input("숫자를 공백으로 구분해서 입력하세요.").strip()
        if not input_str:
            print("잘못된 입력입니다.")
            return
        
        numbers = [float(num) for num in input_str.split()]
    except ValueError:
        print("잘못된 입력입니다.")
        return
    
    sorted_numbers = selection_sort(numbers)

    # 출력: 소수점 포함
    print("Sorted:", "".join(str(num) for num in sorted_numbers))

if __name__ == "__main__":
    main()

