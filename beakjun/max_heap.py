# heapq의 default: 최소 힙 (가장 작은 수부터 pop)
import heapq
import sys
input = sys.stdin.readline

N = int(input())
max_heap = []

for i in range (N) :
    a = int(input())
    # 입력받은 수의 부호를 바꿔서 힙에 넣기
    heapq.heappush(max_heap, (-1)*a)

    # 입력받은 수가 0인 경우
    if a == 0 :
        # 힙이 비어있지 않으면
        if max_heap :
            # 가장 작은 수 제거, 부호 바꿔서 출력
            print((-1)*heapq.heappop(max_heap))
        # 힙이 비어있는 경우
        else :
            # 0 출력
            print(0)