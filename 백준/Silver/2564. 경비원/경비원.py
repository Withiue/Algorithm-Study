width, height = map(int, input().split())
n = int(input())
mart = [[0,0] for _ in range(n+1)]
for i in range(n+1): # n번째는 동근이
    mart[i][0], mart[i][1] = map(int, input().split()) # 0은 방향, 1은 거리


answer = 0

for i in range(n):
    if(mart[n][0] == 1):
        # 1, 1
        if(mart[i][0] == 1):
            answer += abs(mart[i][1] - mart[n][1])
        # 1, 2
        elif(mart[i][0] == 2):
            # 왼쪽 통로가 최단 거리이면
            if(mart[i][1] + mart[n][1] < 2 * width - mart[i][1] - mart[n][1]):
                answer += height + mart[i][1] + mart[n][1]
            # 오른쪽이면
            else:
                answer += height + 2 * width - mart[i][1] - mart[n][1]
        # 1, 3
        elif(mart[i][0] == 3):
            answer += mart[i][1] + mart[n][1]
        # 1, 4
        elif(mart[i][0] == 4):
            answer += mart[i][1] + width - mart[n][1]
    elif(mart[n][0] == 2):
        # 2, 1
        if(mart[i][0] == 1):
            # 왼쪽 통로가 최단 거리이면
            if(mart[i][1] + mart[n][1] < 2 * width - mart[i][1] - mart[n][1]):
                answer += height + mart[i][1] + mart[n][1]
            # 오른쪽이면
            else:
                answer += height + 2 * width - mart[i][1] - mart[n][1]
        # 2, 2
        elif(mart[i][0] == 2):
            answer += abs(mart[i][1] - mart[n][1])
        # 2, 3
        elif(mart[i][0] == 3):
            answer += mart[n][1] + height - mart[i][1]
        # 2, 4
        elif(mart[i][0] == 4):
            answer += width - mart[n][1] + height - mart[i][1]
    elif (mart[n][0] == 3):
        # 3, 1
        if(mart[i][0] == 1):
            answer += mart[i][1] + mart[n][1]
        # 3, 2
        elif(mart[i][0] == 2):
            answer += mart[i][1] + height - mart[n][1]
        # 3, 3
        elif(mart[i][0] == 3):
            answer += abs(mart[i][1] - mart[n][1])
        # 3, 4
        elif(mart[i][0] == 4):
            # 위쪽 통로가 최단 거리이면
            if(mart[i][1] + mart[n][1] < 2 * height - mart[i][1] - mart[n][1]):
                answer += width + mart[i][1] + mart[n][1]
            # 아래쪽이면
            else:
                answer += width + (2 * height) - mart[i][1] - mart[n][1]
    elif (mart[n][0] == 4):
        # 4, 1
        if(mart[i][0] == 1):
            answer += mart[n][1] + width - mart[i][1]
        # 4, 2
        elif(mart[i][0] == 2):
            answer += height - mart[n][1] + width - mart[i][1]
        # 4, 3
        elif(mart[i][0] == 3):
            # 위쪽 통로가 최단 거리이면
            if(mart[i][1] + mart[n][1] < 2 * height - mart[i][1] - mart[n][1]):
                answer += width + mart[i][1] + mart[n][1]
            # 아래쪽이면
            else:
                answer += width + (2 * height) - mart[i][1] - mart[n][1]
        # 4, 4
        elif(mart[i][0] == 4):
            answer += abs(mart[i][1] - mart[n][1])


print(answer)