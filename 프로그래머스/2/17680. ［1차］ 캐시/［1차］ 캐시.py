# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
# LRU, hit은 +1, miss는 +5

def solution(cacheSize, cities):
    time = 0  # 실행시간
    cache = []  # 캐시 [오래된거 -> 최신거 순서]
    
    # 캐시 사이즈가 0인 예외 케이스는 모든게 cache miss, 실행시간 5이다.
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()  # 대소문자 구분 안함
        
        # cache hit일 경우, 기존걸 빼서 다시 뒤에 넣는다.
        if city in cache:
            time += 1
            cache.remove(city)
        
        # cache miss일 경우, 현재 도시 이름을 맨 뒤에 넣는다.
        else:
            time += 5
            if len(cache) == cacheSize:  # 캐시가 꽉 찼으면 가장 오래된걸 빼기
                cache.pop(0)
                
        cache.append(city)
        
    return time