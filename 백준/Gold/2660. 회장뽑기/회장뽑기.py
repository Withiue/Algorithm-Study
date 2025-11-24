from collections import deque

N = int(input())  # 회원 수 입력받기
friend = [[] for _ in range(N + 1)]  # 회원 번호: [해당 회원과 친구인 회원 번호들]
# 친구 회원번호 입력받기
# 마지막 입력받기
while True:
    mem1, mem2 = map(int, input().split())

    if mem1 == -1 and mem2 == -1: break  # -1, -1 입력받으면 while문 빠져나가기

    friend[mem1].append(mem2)
    friend[mem2].append(mem1)  # 양방향 입력

# dist - 회원 번호: 회원으로부터 가장 멀리 떨어져 있는 회원의 거리(==점수)

def bfs(start):  # 초기값
    # 제일 끝으로 방문한 dist값이 해당 회원의 점수임.
    # visited도 체크
    # bfs 초기화
    dist = [-1] * (N + 1)
    Q = deque([start])
    dist[start] = 0

    while Q:
        curMem = Q.popleft()
        for nextMem in friend[curMem]:
            if dist[nextMem] != -1: continue  # nextMem을 이미 방문했으면 pass
            Q.append(nextMem)  # 큐에 다음거 넣기
            dist[nextMem] = dist[curMem] + 1  # 거리값 갱신하기

    # 최대 dist값 리턴하기
    return max(dist)

# 각 회원 번호마다 bfs 돌려서 점수 구하기
score_list = [21e9] * (N + 1)
for i in range(1, N + 1):
    score = bfs(i)  # 1 ~ N번까지
    score_list[i] = score

# 회장 후보의 점수, 후보의 수 출력하기
min_score = min(score_list)
cnt = 0
ans_list = []
for i in range(1, N + 1):
    if score_list[i] == min_score:
        cnt += 1
        ans_list.append(i)
print(min_score, cnt)

# 회장 후보를 오름차순으로 출력
sorted(ans_list)
print(*ans_list)