from collections import deque

# N: 미로를 구성하는 줄의 수, M: 미로를 구성하는 정수의 수
N, M = map(int, input().split())
# 미로 생성
graph = []

# 미로를 구성하는 데이터 입력
for _ in range (N) :
    graph.append(list(map(int, input())))

# 최단 거리 -> bfs 활용
def bfs(x, y) :

    # 이동할 4가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐 생성 (deque() 활용하여 각 문자가 요소로 된 리스트 생성)
    queue = deque()
    # 큐에 데이터 삽입
    queue.append((x, y))

    while queue :
        # 큐 내부 데이터 꺼내기
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어날 경우, 이동하지 않음
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue

            # 벽(0)을 만난 경우, 이동하지 않음
            if graph[nx][ny] == 0 :
                continue

            # 이동 가능한 칸(1)을 만난 경우
            if graph[nx][ny] == 1 :
                # 이전 값에 1 더하기
                graph[nx][ny] = graph[x][y] + 1
                # 큐에 현재 위치 값 삽입
                queue.append((nx, ny))

    # 최소 칸 수가 저장되어 있는 graph[N-1][M-1] 반환
    return graph[N-1][M-1]

print(bfs(0, 0))