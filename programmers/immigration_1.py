def solution(n, times):
    # 입국 심사를 기다리는 사람 수 (최소) * 각 심사관이 한 명을 심사하는데 걸리는 시간 (최소)
    left = 1
    # 입국 심사를 기다리는 사람 수 (최대) * 각 심사관이 한 명을 심사하는데 걸리는 시간 (최대)
    right = n * max(times)


    # 심사 시간을 구하는 동안 left는 right보다 항상 작아야 함
    while (left < right) :
        # 입국 심사를 받은 사람
        people = 0
        # 기준이 될 중간 값
        mid = (left + right) // 2

        for i in times :
            # 심사를 받은 사람 수 += 입국 심사에 소요되는 시간 // 한 명을 심사하는데 걸리는 시간
            people += mid // i
            
            # 입국 심사를 받은 사람의 수 >= 입국 심사를 받아야 할 사람의 수
            if people >= n :
                # 반복문 종료
                break;

        # 범위 내에서 더 이상 입국 심사를 받을 사람이 없는 경우
        if (people >= n) :
            answer = mid
            # right 값 옮겨서 범위 좁히기
            right = mid

        # 범위 내에서 입국 심사를 받을 사람이 남은 경우
        else :
            # left 값을 mid 다음 값으로 옮겨서 범위 늘리기
            left = mid + 1

    return answer

print(solution(6, [7, 10]))