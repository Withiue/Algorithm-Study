# 각 폰켓몬 종류 리스트 nums
# 가장 다양한 종류(최대 종류)의 폰켓몬 원함
# 최대 종류 번호의 개수 return

# 1. set()으로 중복 제거 후, nums의 종류의 개수 세기(=cnt)
# 2. cnt와 N / 2 비교
# 2-1. cnt가 N / 2보다 작으면 cnt만큼 return 
# 2-2. cnt가 N / 2보다 크면 N / 2만큼 return

from collections import Counter

def solution(nums):
    N = len(nums)  # 총 폰켓몬 마리수
    
    # 1. set()으로 중복 제거 후, nums의 종류의 개수 세기
    cnt = len(set(nums))
    
    # 2. cnt와 N / 2 비교
    if cnt < N / 2:  # 2-1. cnt가 N / 2보다 작으면 cnt만큼 return 
        return cnt
    else:  # 2-2. cnt가 N / 2보다 크면 N / 2만큼 return
        return N / 2