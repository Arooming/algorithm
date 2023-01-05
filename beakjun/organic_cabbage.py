from collections import deque

T = int(input())
# 지렁이들의 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b) :
    queue = deque()
    # 큐에 배추밭 위치 데이터 삽입
    queue.append((a, b))
    # 배추밭 방문처리
    matrix[a][b] = 0

    while queue :
        # 큐 내부의 왼쪽 데이터를 pop하여 x, y에 저장
        x, y = queue.popleft()

        # 지렁이 이동 제한
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 범위를 넘어설 경우 continue
            if nx < 0 or nx >= M or ny < 0 or ny >= N :
                continue
            
            # 배추가 심어진 곳을 만난 경우
            if matrix[nx][ny] == 1 :
                # 큐에 해당 위치 데이터 저장
                queue.append((nx, ny))
                # 해당 위치 방문처리
                matrix[nx][ny] = 0

# 테스트 케이스 갯수에 따라 반복
for i in range (T) :
    # M: 배추밭 가로 길이, N: 배추밭 세로 길이, K: 배추가 심어진 위치 개수
    M, N, K = map(int, input().split())
    # 배추밭의 가로, 세로 길이에 맞춰 영행렬 생성
    matrix = [[0]*(N) for _ in range (M)]
    # 지렁이의 마리 수를 체크할 변수
    count = 0

    # 배추가 심어진 위치 갯수에 따라 반복
    for j in range (K) :
        # x, y: 배추가 심어진 위치
        x, y = map(int, input().split())
        # 배추가 심어진 부분은 1로 체크
        matrix[x][y] = 1

    # 배추가 심어져있다면, bfs() 실행하고 지렁이 수 + 1
    for a in range (M) :
        for b in range (N) :
            if matrix[a][b] == 1 :
                bfs(a, b)
                count += 1
    
    # 각 테스트 케이스에 필요한 지렁이 수 출력
    print(count)