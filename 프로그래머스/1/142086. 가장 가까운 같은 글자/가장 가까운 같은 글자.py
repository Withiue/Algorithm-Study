def solution(s):
    answer = [-1]  # 첫 글자는 무조건 -1
    
    for i in range(1, len(s)):
        # 자신의 앞에 같은 글자가 있는지 확인
        for j in range(i-1, -1, -1):  # i로부터 한 칸씩 앞으로
            if s[i] == s[j]:  # 같은 글자 있으면 그 글자만큼 append
                answer.append(i-j)
                break
        # 같은 글자 없으면 -1 추가
        else:
            answer.append(-1)    
    return answer