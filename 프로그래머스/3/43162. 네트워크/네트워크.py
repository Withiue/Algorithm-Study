def dfs(computers, visited, node):  # node는 시작노드
    visited[node] = True  # 현재 노드 방문 처리
    
    for idx, connected in enumerate(computers[node]):
        if connected and not visited[idx]:  # 연결되어 있으며 방문하지 않은 노드라면
            dfs(computers, visited, idx)  # 해당 노드를 방문하러 이동

def solution(n, computers):
    answer = 0
    
    visited = [False] * n  # 방문 여부를 저장하는 리스트
    
    # computers 순회 통해 이어진 것 표시하기
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1  # dfs로 연결된 노드들을 모두 방문하면서 네트워크 개수 증가
    
    return answer