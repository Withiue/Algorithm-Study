T = 4

for tc in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    
    if (x1 > p2) or (y1 > q2) or (p1 < x2) or (q1 < y2) :
        print('d')
        continue
    elif y1 == q2 or q1 == y2:  # y축이 평행일 때
        if x1 == p2 or p1 == x2:  # x축이 평행일 때
            print('c')
            continue
        else:  # y축만 평행일 때
            print('b')
            continue
    elif x1 == p2 or p1 == x2:  # x축만 평행일 때
        print('b')
        continue
    else:
        print('a')
        continue