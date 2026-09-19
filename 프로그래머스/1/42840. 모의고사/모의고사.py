def solution(answers):
    answer = []
    
    # 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 맞힌 개수
    correct_lst = [0, 0, 0]
    
    # 정답 수 만큼 p1, p2, p3 반복하기
    n = len(answers)
    for i in range(n):
        # 가장 많은 문제를 맞힌 사람 배열에 담기
        if answers[i] == p1[i % len(p1)]:
            correct_lst[0] += 1
        if answers[i] == p2[i % len(p2)]:
            correct_lst[1] += 1
        if answers[i] == p3[i % len(p3)]:
            correct_lst[2] += 1
    
    max_n = max(correct_lst)
    
    for i in range(3):
        if correct_lst[i] == max_n:
            answer.append(i+1)
    
    return answer