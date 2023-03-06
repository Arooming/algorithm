import sys
input = sys.stdin.readline

def solution(n, times):
    # 입국 심사를 기다리는 사람 수 (최소) * 각 심사관이 한 명을 심사하는데 걸리는 시간 (최소)
    left = 1
    # 입국 심사를 기다리는 사람 수 (최대) * 각 심사관이 한 명을 심사하는데 걸리는 시간 (최대)
    right = n * max(times)

    def isPossible (target) :
        n = waiting
        # times: 한 명을 심사하는데 걸리는 시간
        for i in times :
            # 기다리는 사람 수 -= 입국 심사에 소요되는 시간 / 한 명을 심사하는데 걸리는 시간
            n -= target//i
        # 주어진 범위 내에서 더 이상 입국 심사를 받을 사람이 없는 경우
        return n <= 0

    # 심사 시간을 구하는 동안 left는 right보다 항상 작아야 함
    while (left < right) :
        waiting = n

        # 기준이 될 중간 값
        mid = (left + right) // 2

        if (isPossible(mid)) :
            # right 값 옮겨서 범위 좁히기
            right = mid

        # 범위 내에서 입국 심사를 받을 사람이 남은 경우
        else :
            # left 값을 mid 다음 값으로 옮겨서 범위 늘리기
            left = mid + 1

    return left

print(solution(6, [7, 10]))