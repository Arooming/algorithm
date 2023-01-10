import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
idx = []
pre_sum = []

idx.append([0, 0])
for _ in range (1, M+1) :
    idx.append(list(map(int, input().split())))

# print("idx: ", idx)

pre_sum.append(0)
for u in range (1, N+1) :
    pre_sum.append(pre_sum[u-1] + arr[u])

# print("pre_sum: ", pre_sum)

for v in range (1, M+1) :
    i = idx[v][0]
    j = idx[v][1]
    # print("result: ", pre_sum[j] - pre_sum[i-1])
    result = pre_sum[j] - pre_sum[i-1]
    print(result)