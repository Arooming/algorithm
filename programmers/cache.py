from collections import deque

def solution(cacheSize, cities) :
    # 큐의 최대 크기를 cacheSize에 맞춰줌
    queue = deque(maxlen = cacheSize)
    # 실행 시간
    time = 0

    for i in cities :
        # 대소문자 구분을 하지 않으므로, 도시를 모두 대문자(소문자)로 바꿔줌
        i = i.upper()

        # cacheSize가 0인 경우
        if cacheSize == 0 :
            # cities 배열 크기에 5를 곱한 값 리턴
            return len(cities) * 5
        
        # cacheSize가 0이 아닌 경우
        else :
            # 큐에 도시 i가 있다면
            if i in queue :
                # 이전에 있던 같은 도시를 빼고
                queue.remove(i)
                # cache hit
                time += 1
                # 큐에 도시 i 추가
                queue.append(i)
            
            # 큐에 도시 i가 없다면
            else :
                # cacheSize보다 큐의 크기가 크거나 같아진 경우
                if cacheSize <= len(queue) :
                    # 큐의 가장 왼쪽에 있는 데이터 제거
                    queue.popleft()
                # cache miss
                time += 5
                # 큐에 도시 i 추가
                queue.append(i)
    
    # 실행시간 리턴
    return time
