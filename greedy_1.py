# N: 동전의 종류, K: 동전 가치의 합
N, K = map(int, input().split())
# 동전의 가치를 저장할 리스트 생성
coin_list = list()

# 입력받은 동전을 동전 리스트에 저장
for i in range(N) :
    coin = int(input())
    coin_list.append(coin)

count = 0
# 리스트에 저장된 동전 중, 가장 가치가 큰 것부터 반복문 실행
for i in reversed (coin_list) :
    # 동전 가치의 합(K)을 동전 리스트에 저장된 값(i)으로 나눈 몫은 count에 더하기
    # 동전 가치의 합(K)을 동전 리스트에 저장된 값(i)으로 나눈 나머지 값은 K에 부여하기
    count += K // i
    K %= i

print(count)