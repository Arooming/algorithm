from collections import deque
import sys
# 같은 코드에서도 input()으로 받느냐, readline()으로 받느냐에 따라 결과가 달라짐
# input()으로 받으면 시간초과로 아예 결과값을 얻을 수 없음
# readline()으로 받으면 원하는 결과값을 얻을 수 있음
input = sys.stdin.readline

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

    
def bfs(V) :
    # 시간초과 방지를 위해 deque() 활용
    queue = deque()
    # 큐에 데이터 삽입
    queue.append(V)
    # 방문 표시
    visited[V] = 1

    while queue:
        # 큐 내부 데이터 빼내서 변수 x에 저장
        x = queue.popleft()
        
        # graph[x]를 돌면서
        for i in graph[x] :
            # 방문 표시가 되어있지 않다면
            if visited[i] == 0:
                # 큐에 해당 데이터 추가
                queue.append(i)
                # 방문 표시
                visited[i] = 1
                

# 1부터 N+1까지 반복문 돌면서
for i in range (1, N+1) :
    # 해당 위치를 아직 방문하지 않았다면
    if visited[i] == 0:
        # 해당 위치 정보를 매개변수로 하여 bfs() 실행
        bfs(i)
        # 연결 요소 개수 추가
        count += 1

print(count)