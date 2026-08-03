def solution(arr):
    answer = [0, 0]  # [0 개수, 1 개수]
    
    n = len(arr)
    
    # 압축 함수
    def recur(n, x, y):  # 현재 길이, 좌상 시작 좌표
        # 멈추는 조건 - 칸이 딱 하나면 그대로 return하기
        if n == 1: 
            if arr[x][y] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
            return
        
        # 압축 조건 - 내부에 있는 모든 수가 같은 값이면 해당 수로 압축
        isFalse = False
        for i in range(n):
            for j in range(n):
                if arr[x][y] != arr[x+i][y+j]:
                    isFalse = True
                    break
            if isFalse: break
            
        else:
            if arr[x][y] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
            return
        
        # 4분할로 재귀하기
        half = n // 2
        
        recur(half, x, y)  # 좌상
        recur(half, x + half, y)  # 우상
        recur(half, x, y + half)  # 좌하
        recur(half, x + half, y + half)  # 우하
        
    recur(n, 0, 0)
    
    return answer