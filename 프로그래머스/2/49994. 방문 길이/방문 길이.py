def solution(dirs):    
    D = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    # 초기화
    visited = set()  # ((현재좌표), (다음좌표)) 넣기, set으로 중복 제거
    curX, curY = 0, 0

    for d in dirs:
        plus_x, plus_y = D[d]  # 방향에 따른 증가값 구하기
        nX = curX + plus_x
        nY = curY + plus_y
        
        tmp = tuple(sorted(((curX, curY), (nX, nY))))  # sorted()의 결과는 list
        
        # 좌표 밖이면 pass
        if nX < -5 or nX > 5 or nY < -5 or nY > 5:
            continue
            
        # 없으면 visited에 넣고 cur 좌표로 바꾸기
        visited.add(tmp)
        curX, curY = nX, nY

    # len(visited) return하기
    return len(visited)