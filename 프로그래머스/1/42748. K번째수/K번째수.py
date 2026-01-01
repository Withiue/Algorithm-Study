def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 자르기
        sliced_array = array[i-1:j]
        print(sliced_array)
        # 정렬하기
        sliced_array.sort()
        print(sliced_array)
        # k번째 숫자
        num = sliced_array[k-1]
        print(num)
        answer.append(num)
    return answer