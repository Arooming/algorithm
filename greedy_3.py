# 줄을 선 사람의 수
N = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간을 담을 리스트
person = list(map(int, input().split()))
# 리스트 오름차순 정렬
person.sort()

sum = 0
min_time = 0

for i in (person) :
    # 각 사람이 돈을 인출하는데 필요한 시간
    sum += i
    # 각 사람이 돈을 인출하는데 필요한 시간의 합
    min_time += sum

print(min_time)