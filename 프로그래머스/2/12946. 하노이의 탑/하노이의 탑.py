# 하노이의 탑 - 스택 활용, list로 stack 구현

def solution(n):
    answer = []
    
    # 1의 원판 n개를 3으로 n개 옮기는 함수
    def hanoi(n, start, end, via):
        # 종료조건
        if n == 1:
            answer.append([start, end])
            return
        
        # 재귀
        # 1. 기둥2에 기둥1의 원판 n-1개 옮기기
        hanoi(n - 1, start, via, end)
        
        # 2. 기둥1 맨 밑 원판 기둥3으로 옮기기
        answer.append([start, end])
        
        # 3. 기둥2 원판 n-1개 기둥3으로 옮기기
        hanoi(n - 1, via, end, start)
        
    hanoi(n, 1, 3, 2)
    
    return answer