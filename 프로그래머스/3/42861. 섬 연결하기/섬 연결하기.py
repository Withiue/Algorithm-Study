from heapq import heappush, heappop

    

def solution(n, costs):
    # 인접 행렬 초기화
    graph = [[0] * n for _ in range(n)]
    
    # 간선 정보를 인접 행렬에 기록
    for u, v, w in costs:
        graph[u][v] = w
        graph[v][u] = w  # 무방향 그래프이니까 양방향 기록
        
    # 특정 정점 기준으로 시작
    # 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
    # 작은 노드를 먼저 꺼내기 위해 우선순위 큐 활용
    def prim(start_node):
        pq = [(0, start_node)]  # (가중치, 노드) 형태, 자기 자신으로 가는 가중치는 0
        MST = [0] * n  # visited
        min_weight = 0  # 최소 비용
        count = 0  # 연결된 노드 수
        
        while pq:
            # 현재 갈 수 있는 노드 중 가중치가 가장 작은 것 추출
            weight, node = heappop(pq)
            
            # 이미 방문한 노드(이미 MST에 포함된 노드)라면 스킵
            if MST[node]:
                continue
                
            # 방문 처리 및 가중치 합산
            MST[node] = 1
            min_weight += weight
            count += 1
            
            # 모든 노드를 찾았다면 조기 종료 가능
            if count == n:
                break
            
            # 현재 노드와 연결된 다른 노드들을 탐색
            for next_node in range(n):
                # 연결이 안 되어 있거나(0), 이미 MST에 포함된 노드라면 스킵
                if graph[node][next_node] == 0 or MST[next_node]:
                    continue
                
                # 다음 후보 노드를 우선순위 큐에 삽입
                # BFS와 다르게 여기서 방문 처리를 하지 않는 것이 핵심!
                # 더 저렴한 가중치를 가진 경로가 나중에 나올 수 있기 때문
                heappush(pq, (graph[node][next_node], next_node))
        return min_weight
            

    # 어느 정점에서 시작해도 최소 신장 트리의 비용은 동일함
    return prim(0)