N = int(input())

# board[100][100]
board = [[0] * 101 for _ in range(101)]

for n in range(N):
    x, y = map(int, input().split())
    # x부터 +10칸 1로 바꾸기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
       if(board[i][j] == 1):
           cnt += 1
print(cnt) 