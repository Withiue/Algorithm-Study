from collections import Counter

def solution(points, routes):
    answer = 0
    every_routes = []

    # 로봇 하나씩
    for i in range(len(routes)):
        
        time = 0

        # 첫 위치
        first_point = routes[i][0] - 1
        cur_r, cur_c = points[first_point]

        every_routes.append((time, cur_r, cur_c))

        # 현재 포인트 -> 다음 포인트
        for j in range(len(routes[i]) - 1):

            end = routes[i][j + 1] - 1
            end_r, end_c = points[end]

            # 다음 포인트까지 r 이동
            while cur_r != end_r:
                # cur_r를 end_r 방향으로 한 칸 이동
                if cur_r < end_r:
                    cur_r += 1
                else:
                    cur_r -=1
                
                time += 1
                every_routes.append((time, cur_r, cur_c))

            # 그 다음 c 이동
            while cur_c != end_c:
                # cur_c를 end_c 방향으로 한 칸 이동
                if cur_c < end_c:
                    cur_c += 1
                else:
                    cur_c -=1
                
                time += 1
                every_routes.append((time, cur_r, cur_c))
    
    
    # Counter.item() return하기
    counter_routes = Counter(every_routes)
    
    for key, value in counter_routes.items():
        if value >= 2:  # 로봇이 같은 시간에 두 대 이상 충돌하면 answer += 1
            answer += 1
    
    return answer