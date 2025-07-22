# board = [1002][1002] -1로 초기화
# n 입력받기
# for 색종이순서 n번 반복
#     x, y, width, height = map으로 입력받기
#     for width
#         for height
#             board[x][y] = 색종이순서 값 대입하기

# for 색종이순서 n번 반복
#     cnt = 0
#     board[1002][1002]를 for문 돌아서 색종이순서-1인거 있으면 cnt+=1하기
#     print(cnt)

board = [[-1 for _ in range(1002)] for _ in range(1002)]

n = int(input())

for i in range(n): # 0~n-1
    x, y, width, height = map(int, input().split())
    for w in range(width):
        for h in range(height):
            board[x+w][y+h] = i

for i in range(n): # 0~n-1
    cnt = 0
    for a in range(1002):
        for b in range(1002):
            if(board[a][b] == i):
                cnt += 1
    print(cnt)