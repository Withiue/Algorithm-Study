N = int(input())

for i in range(1, N + 1):
    a_cnt = [0 for _ in range(5)]
    b_cnt = [0 for _ in range(5)]

    # a 입력받기
    a_input = list(map(int, input().split()))
    # b 입력받기
    b_input = list(map(int, input().split()))

    # a_cnt에 도형별로 수 세어서 +1 하기
    for a in range(a_input[0]):
        a_cnt[a_input[a + 1]] += 1

    # b_cnt에 도형별로 수 세어서 +1 하기
    for b in range(b_input[0]):
        b_cnt[b_input[b + 1]] += 1

    # a, b 비교하기
    # 4 비교
    if (a_cnt[4] > b_cnt[4]):
        print('A')
    elif (a_cnt[4] < b_cnt[4]):
        print('B')
    elif (a_cnt[4] == b_cnt[4]):
        # 3 비교
        if (a_cnt[3] > b_cnt[3]):
            print('A')
        elif (a_cnt[3] < b_cnt[3]):
            print('B')
        elif (a_cnt[3] == b_cnt[3]):
            # 2 비교
            if (a_cnt[2] > b_cnt[2]):
                print('A')
            elif (a_cnt[2] < b_cnt[2]):
                print('B')
            elif (a_cnt[2] == b_cnt[2]):
                # 1 비교
                if (a_cnt[1] > b_cnt[1]):
                    print('A')
                elif (a_cnt[1] < b_cnt[1]):
                    print('B')
                elif (a_cnt[1] == b_cnt[1]):
                    # 무승부
                    print('D')
