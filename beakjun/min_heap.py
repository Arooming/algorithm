# heapq의 default: 최소 힙 (가장 작은 수부터 pop)
import heapq
import sys
input = sys.stdin.readline

N = int(input())
min_heap = []

for i in range (N) :
    a = int(input())

    # 입력받은 수가 0인 경우
    if a == 0 :
        # 힙이 비어있지 않으면
        if min_heap :
            # 가장 작은 수 제거, 출력
            print(heapq.heappop(min_heap))
        # 힙이 비어있는 경우
        else :
            # 0 출력
            print(0)
    
    # 입력받은 수가 0이 아닌 경우
    else:
        # 힙에 데이터 넣기
        heapq.heappush(min_heap, a)