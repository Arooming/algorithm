# 입력식에서 '-' 분리
cal = input().split('-')
nums = []

for i in (cal) :
    sum = 0
    # '-'를 분리한 입력식에서 '+' 분리
    for j in (i.split('+')) :
        # 해당 값을 정수로 변환하여 더하기
        sum += int(j)
    # 리스트에 추가
    nums.append(sum)

final = nums[0]

# 리스트에 저장된 0번째 숫자에서 1번째 숫자부터 저장된 모든 수 빼기
for i in (nums[1:]) :
    final -= i

print(final)