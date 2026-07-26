def solution(numbers):
    answer = []
    for n in numbers:
        # 짝수인 경우 -> +1 return
        if n % 2 == 0:
            answer.append(n+1)
            continue
        
        # 홀수인 경우
        # 오른쪽에서 가장 가까운 0과 그 오른쪽 1을 01 → 10으로 변경
        else:
            binary = '0' + bin(n)[2:]
            
            i = binary.rfind('0')
            
            binary = binary[:i] + '10' + binary[i + 2:]
            
            answer.append(int(binary, 2))
    return answer