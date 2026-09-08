import heapq

def solution(N, road, K):
    # 마을 연결 정보
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    # 1번 마을에서 각 마을까지의 최단거리
    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    # (거리, 마을번호)
    q = []
    heapq.heappush(q, (0, 1))

    while q:
        cur_dist, cur = heapq.heappop(q)

        # 이미 더 짧은 경로를 찾았다면 넘어가기
        if cur_dist > distance[cur]:
            continue

        # 현재 마을과 연결된 마을 확인
        for next_node, cost in graph[cur]:
            new_dist = cur_dist + cost

            # 더 짧은 경로를 발견했다면 갱신
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    # K시간 이하로 갈 수 있는 마을 개수
    answer = 0

    for dist in distance[1:]:
        if dist <= K:
            answer += 1

    return answer