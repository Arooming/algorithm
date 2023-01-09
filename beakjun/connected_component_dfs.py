import sys
# 시간 초과 방지를 위해 readline() 활용
input = sys.stdin.readline
# python은 재귀를 제한 -> setrecursionlimit() 활용하여 허용 범위 늘려주기
sys.setrecursionlimit(10**7)

# N: 정점의 개수, M: 간선의 개수
N, M = map(int, input().split())
# 빈 그래프 생성
graph = [[] for _ in range (N+1)]
# 방문 표시를 위한 변수 visited 생성
visited = [0] * (N+1)
# 연결 요소의 개수
count = 0

# 간선의 개수만큼 반복문 실행
for _ in range (M) :
    # 간선의 양 끝점
    u, v = map(int, input().split())
    # 무방향 그래프를 인접 리스트로 구현 시, 
    # 간선 추가될 때마다 정점의 인접리스트에 각각 반대편 정점 노드 추가해야 함
    graph[u].append(v)
    graph[v].append(u)

def dfs(V) :
    # 방문 표시 
    visited[V] = 1

    # 그래프를 돌면서
    for i in graph[V] :
        # 아직 방문하지 않았다면
        if visited[i] == 0 :
            # 해당 위치에서 dfs() 실행 (재귀)
            dfs(i)

# 1부터 N+1까지 반복문 돌면서
for i in range (1, N+1) :
    # 아직 방문하지 않았다면
    if visited[i] == 0 :
        # dfs() 실행
        dfs(i)
        # 연결요소 개수 추가
        count += 1
        
print(count)