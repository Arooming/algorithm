# 회의의 수: N
N = int(input())
# 회의의 시작 시간과 끝나는 시간 정보를 저장할 리스트
meetings = list()

# 리스트에 회의 시작 시간과 끝나는 시간 정보 입력 받아 저장
for i in range (N) :
    start, end = map(int, input().split())
    meetings.append([start, end])

# meetings의 x[0] 오름차순 정렬 (start 오름차순 정렬)
meetings = sorted(meetings, key = lambda x: x[0])
# meetings의 x[1] 오름차순 정렬 (end 오름차순 정렬)
meetings = sorted(meetings, key = lambda x: x[1])

end_time = 0
count = 0
for i in (meetings) :
    # meetings의 start 값이 end_time에 저장된 값보다 크거나 같은 경우
    if (i[0] >= end_time) :
        # 사용 가능한 회의 개수 추가
        count += 1
        # end_time에 meetings의 end 값 부여하기
        end_time = i[1]

print(count)