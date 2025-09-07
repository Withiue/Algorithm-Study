def enqueue(n):
    global rear
    rear += 1
    Q[rear] = n

def dequeue():
    global front
    front += 1
    return Q[front]

def isEmpty():
    global front, rear
    return front == rear



N = int(input())    # 컴퓨터 개수
connected = int(input())    # 컴퓨터 연결된 횟수
network = [[] for _ in range(N + 1)]     # 인덱스는 출발 컴퓨터 번호, 값은 연결된 컴퓨터 번호
visited = [0] * (N + 1)

# 연결 입력받기
for i in range(connected):
    s, e = map(int, input().split())
    # 0이면 그냥 넣고 아니면 append하기
    if network[s] == 0:
        network[s] = [e]
        network[e] = [s]
    else:
        network[s].append(e)
        network[e].append(s)

# bfs
Q = [0] * 102
front = rear = -1

# 시작점인 1 넣기
enqueue(1)
visited[1] = 1

answer = 0  # 바이러스에 걸리게 되는 컴퓨터의 수
while not isEmpty():
    # 큐 빌때까지 bfs 돌기
    # 현재꺼 꺼내서 탐색하고 다음으로 넘어가기
    cur = dequeue()
    if network[cur]:
        for e in network[cur]:
            if not visited[e]:
                answer += 1
                visited[e] = 1
                enqueue(e)

print(answer)