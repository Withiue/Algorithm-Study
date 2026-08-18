from math import gcd

def solution(arrayA, arrayB):
    a = 0
    
    # arrayA 전체의 최대공약수
    gcdA = arrayA[0]
    for num in arrayA[1:]:
        gcdA = gcd(gcdA, num)
    
    # arrayB 전체의 최대공약수
    gcdB = arrayB[0]
    for num in arrayB[1:]:
        gcdB =  gcd(gcdB, num)
        
    # gcdA가 arrayB 중에 나눠지는 수가 없는지 확인
    if all(num % gcdA != 0 for num in arrayB):
        a = max(a, gcdA)
    
    # gcdB가 arrayA 중에 나눠지는 수가 없는지 확인
    if all(num % gcdB != 0 for num in arrayA):
        a = max(a, gcdB)
    
    return a