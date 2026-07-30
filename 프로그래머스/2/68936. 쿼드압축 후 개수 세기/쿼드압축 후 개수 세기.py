# 크기 몇인지 세기

# 압축하기
# 다 같나? -> 그러면 해당 수로 압축
# 다 같지 않으면 4등분 해서 재귀함수 들어감
# 한 칸만 남았을때는 그대로 리턴하기

def recur(arr, x1, y1, size, answer):
    first = arr[x1][y1]
    
    # 현재 구역이 모두 같은 숫자인가?
    same = True
    
    for i in range(x1, x1 + size):
        for j in range(y1, y1 + size):
            if arr[i][j] != first:
                same = False
                break
        
        if not same:
            break
    
    # 모두 같으면 하나로 압축
    if same:
        answer[first] += 1
        return
    
    # 모두 같지 않으면 4등분
    half = size // 2
    
    recur(arr, x1, y1, half, answer)  # 왼쪽 위
    recur(arr, x1, y1 + half, half, answer)  # 오른쪽 위
    recur(arr, x1 + half, y1, half, answer)  # 왼쪽 아래
    recur(arr, x1 + half, y1 + half, half, answer)  # 오른쪽 아래

def solution(arr):
    answer = [0, 0]
    
    recur(arr, 0, 0, len(arr), answer)
    
    return answer