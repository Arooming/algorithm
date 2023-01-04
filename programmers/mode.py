from collections import Counter

def solution(array) :
    # 배열 원소의 등장 횟수 내림차순 정렬
    mode = Counter(array).most_common()
    # 가장 많이 측정된 횟수를 변수 MAX에 저장
    MAX = mode[0][1]

    # 배열의 원소가 하나이거나 한개의 최빈값을 가지는 경우
    if len(mode) == 1 or mode[1][1] != MAX :
        # 최빈값 반환
        return mode[0][0]
    # 두개 이상의 최빈값을 가지는 경우
    else :
        # -1 반환
        return -1