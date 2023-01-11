import sys
# 시간 단축을 위해 input() 대신 readline() 사용
input = sys.stdin.readline

# N: 정수의 개수, M: 합을 구해야하는 횟수
N, M = map(int, input().split())
# arr: N개의 수를 저장할 리스트
arr = list(map(int, input().split()))
# pre_sum: 배열에 저장된 데이터의 합을 저장할 리스트
# 해당 리스트의 첫번째 데이터로 0 저장
pre_sum = [0]

# 시간이 더 걸리는 풀이
# for i in range (N) :
    # # arr에 저장된 데이터와 pre_sum에 저장된 데이터의 합을 pre_sum에 삽입
    # pre_sum.append(arr[i] + pre_sum[i])

# 시간을 더 단축할 수 있는 풀이
sum = 0
# 배열을 돌면서
for i in (arr) :
    # sum에 i(arr에 저장된 데이터)를 더한 값을 sum에 저장
    sum += i
    # sum에 저장된 값을 pre_sum에 삽입
    pre_sum.append(sum)

# M만큼 반복문 돌면서
for _ in range (1, M+1) :
    # 합을 계산할 구간 입력 받기
    i, j = map(int, input().split())
    # pre_sum에 저장된 j번째 데이터에서 (i-1)번째 데이터를 뺀 값 출력
    # 해당 값이 i번째 수부터 j번째 수까지의 합과 동일함
    print(pre_sum[j] - pre_sum[i-1])
