import math

def solution(denum1, num1, denum2, num2):
    # 분자 계산
    top = denum1 * num2 + denum2 * num1
    # 분모 계산
    bottom = num1 * num2
    # 위에서 계산한 분자와 분모의 최대 공약수를 변수 n에 저장
    n = math.gcd(top, bottom)
    
    # 최대 공약수가 1인 경우
    if n == 1:
        return [top, bottom]
    
    # 최대 공약수가 1이 아닌 경우
    else :
        # 분자와 분모를 각각 최대 공약수로 나누어 기약 분수 형태로 반환
        return [top/n, bottom/n]