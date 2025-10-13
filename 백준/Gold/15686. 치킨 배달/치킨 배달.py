from itertools import combinations

# n: 도시 크기, m: 선택할 치킨집 개수
n, m = map(int, input().split())

# 도시 정보 입력
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

# 집과 치킨집의 좌표를 저장
houses = []  # 집의 좌표들
chickens = []  # 치킨집의 좌표들

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))  # 집 좌표 저장
        elif city[i][j] == 2:
            chickens.append((i, j))  # 치킨집 좌표 저장

# 치킨 거리 계산 함수
def get_chicken_distance(house, chicken):
    """한 집과 치킨집 사이의 거리(맨해튼 거리) 계산"""
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

# 도시의 치킨 거리 계산 함수
def get_city_chicken_distance(selected_chickens):
    """선택된 치킨집들에 대한 도시의 치킨 거리 계산"""
    total = 0
    for house in houses:
        # 각 집마다 가장 가까운 치킨집과의 거리를 구함
        min_dist = float('inf')
        for chicken in selected_chickens:
            dist = get_chicken_distance(house, chicken)
            min_dist = min(min_dist, dist)
        total += min_dist
    return total

# 모든 치킨집 중에서 m개를 선택하는 조합을 시도
min_city_distance = float('inf')

# combinations를 사용하여 m개의 치킨집을 선택하는 모든 경우의 수 탐색
for selected in combinations(chickens, m):
    # 현재 선택된 치킨집들로 도시의 치킨 거리 계산
    city_distance = get_city_chicken_distance(selected)
    # 최솟값 갱신
    min_city_distance = min(min_city_distance, city_distance)

# 결과 출력
print(min_city_distance)