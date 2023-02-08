import sys
# 시간 단축을 위해 input() 대신 readline 사용
input = sys.stdin.readline

N = int(input())
# 수가 10,000보다 작거나 같기 때문에 (10,000 + 1)개의 칸을 가지고 있는 배열을 만들어줌
arr = [0] * 10001

# N만큼 돌면서 입력받은 숫자(i)에 해당하는 칸(arr[i])의 데이터를 1씩 증가시켜줌
for _ in range (N) :
    i = int(input())
    arr[i] += 1

# 저장된 데이터가 0이 아닐 경우, 한 칸(arr[i])에 저장된 데이터만큼 해당 인덱스(i) 출력
for i in range (10001) :
    if arr[i] != 0 :
        for _ in range (arr[i]) :
            print(i)
    