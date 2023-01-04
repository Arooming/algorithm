from collections import deque

# N: 수빈이의 위치, K: 동생의 위치
N, K = map(int, input().split())
# 수빈이와 동생의 최대 이동 가능 범위
MAX = 10 ** 5
# 방문 체크 위한 변수
visited = [0] * (MAX + 1)

def bfs() :
    # 속도 향상을 위해 deque() 사용
    queue = deque()
    # 큐에 수빈이의 출발 위치 데이터 삽입
    queue.append(N)

    while queue :
        # 큐의 가장 왼쪽 값을 pop하여 변수 x에 저장
        x = queue.popleft()

        # 수빈이의 현재 위치와 동생의 위치가 같은 경우
        if x == K :
            # visited[x] 값 출력
            print(visited[x])
            break

        # 수빈이가 이동 가능한 범위
        for i in (x - 1, x + 1, x * 2) :
            # 해당 위치가 주어진 범위 내에 있고 아직 방문하지 않았다면
            if (0 <= i <= MAX and visited[i] == 0) :
                # 해당 위치에 이동한 시간 표시
                visited[i] = visited[x] + 1
                # 큐에 이동한 위치 데이터 삽입
                queue.append(i)
# bfs 실행
bfs()