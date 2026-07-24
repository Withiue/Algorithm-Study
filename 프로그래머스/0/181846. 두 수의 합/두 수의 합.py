def solution(a, b):
    answer = []
    
    a = a[::-1]
    b = b[::-1]
    
    i = 0
    c = 0  # carry
    
    while i < max(len(a), len(b)):
        ia = int(a[i]) if i < len(a) else 0
        ib = int(b[i]) if i < len(b) else 0
        
        total = ia + ib + c
        
        answer.append(str(total % 10))
        c = total // 10

        i += 1
    
    if c:
        answer.append(str(c))
            
    return ''.join(answer[::-1])