t = int(input())
for tc in range(t):
    maxsum = []
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if n>m:
         B, A = A, B
    
    for k in range (len(B) - len(A) + 1):
         sum = 0
         for j in range(len(A)):
             sum += A[j] * B[j + k]
         maxsum.append(sum)
    print('#{} {}'.format(tc+1, max(maxsum)))