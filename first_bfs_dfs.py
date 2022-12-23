# N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# N+1 개의 인접영행렬 생성
matrix = [[0]*(N+1) for i in range (N+1)]
# 방문 표시할 배열 생성
visited = [0]*(N+1)

# 간선 만들기
for i in range(M) :
    a, b = map(int, input().split())
    # 인접해있다면, matrix[a][b] == 1 and matrix[b][a] == 1 성립 (인접행렬 특성)
    matrix[a][b] = matrix[b][a] = 1

def dfs(V) :
    # 방문한 곳 체크
    visited[V] = 1
    print(V, end = ' ')

    # 방문 체크가 되어 있지 않고 해당 정점과 인접한 경우, 함수 호출 (재귀함수)
    for i in range(1, N+1) :
        if (visited[i] == 0 and matrix[V][i] == 1) :
            dfs(i)

def bfs(V) :
    # bfs를 하기 위한 큐 생성
    queue = [V]
    # 방문 체크 (dfs가 종료되면 1로 방문 체크가 되어있기 때문에, 0으로 방문 체크)
    visited[V] = 0

    # 큐 안에 데이터가 없을 때까지
    while queue :
        # 큐에 저장된 첫번째 데이터 제거 (Queue: First In First Out)
        V = queue.pop(0)
        print(V, end = ' ')

        # 방문 체크가 되어있지 않고 해당 정점과 인접한 경우
        for i in range (1, N+1):
          if (visited[i] == 1 and matrix[V][i] == 1) :
                # 큐에 해당 데이터 삽입
                queue.append(i)
                # 방문 체크
                visited[i] = 0

dfs(V)
print()
bfs(V)