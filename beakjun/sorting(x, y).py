import sys
# 시간 단축을 위해 input 대신 readline 활용
input = sys.stdin.readline

N = int(input())
nums = []

# N개의 좌표(x, y) 받아서 nums에 저장
for _ in range (N) :
    x, y = list(map(int, input().split()))
    nums.append((x, y))

# x 좌표를 기준으로 오름차순 정렬
nums.sort(key = lambda x : x)
# y 좌표를 기준으로 오름차순 정렬
nums.sort(key = lambda y : y)

# nums 돌면서 (x, y) 출력
for i in (nums) :
    print(i[0], i[1])