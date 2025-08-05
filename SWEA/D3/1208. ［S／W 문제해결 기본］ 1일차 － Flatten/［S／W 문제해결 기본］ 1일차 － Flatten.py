# import sys
# sys.stdin = open("input (2).txt")

# max()
def my_max(lst):
    my_m = 0
    my_idx = 0
    for idx in range(len(lst)):
        if my_m < lst[idx]:
            my_m = lst[idx]
            my_idx = idx
    return my_m, my_idx

# min()
def my_min(lst):
    my_m = 100
    my_idx = 0
    for idx in range(len(lst)):
        if my_m > lst[idx]:
            my_m = lst[idx]
            my_idx = idx
    return my_m, my_idx

for tc in range(1, 11):
    N = int(input())  # 덤프 횟수
    arr = list(map(int, input().split()))  # 각 상자의 높이값
    diff = 100  # 최고-최저 차 100으로 초기화

    for i in range(N):
        # max 높이 찾기
        max_h, max_idx = my_max(arr)

        # min 높이 찾기
        min_h, min_idx = my_min(arr)

        # 검증: max - min이 0 또는 1이면 그대로 0 또는 1을 반환하고 break
        if max_h - min_h <= 1:
            break

        # max - 1, min + 1 하기 (평탄화)
        arr[max_idx] -= 1
        arr[min_idx] += 1
        # 다시 위에서부터 반복

    # 최종 차이 (Flatten 끝나고 한 번 더 min, max 갱신
    max_h, max_idx = my_max(arr)
    min_h, min_idx = my_min(arr)
    diff = max_h - min_h

    print(f"#{tc} {diff}")
