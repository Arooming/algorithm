import sys
# 시간 단축하기 위해 readline 사용
input = sys.stdin.readline
# 정렬할 수의 개수
N = int(input())
# 정렬할 수를 담을 리스트
nums = []

for _ in range (N) :
    # 수를 입력받아 리스트에 넣기
    nums.append(int(input()))

# 리스트에 들어있는 수를 오름차순 정리
nums.sort()

# print(* list): Unpacking - 인자들을 일일히 넘기는 효과
# []와 , 없이 리스트 요소와 공백만으로 구성된 결과가 출력됨
print(* (nums))