# N: 도시의 개수
N = int(input())

# distance: 도시간의 거리
distance = list(map(int, input().split()))

# price: 주유소의 리터당 가격
price = list(map(int, input().split()))

# min_price: 도시 이동에 필요한 최소비용
min_price = 0

m = price[0]

# 이전 주유 비용이 현재 주유 비용보다 많이 든다면, m에 현재 주유 비용 값 부여
for i in range (N-1) :
    if (m > price[i]) :
        m = price[i]
    # 주유 비용과 도시 간의 거리의 곱을 더하여 최소비용 도출
    min_price += m * distance[i]
    
print(min_price)
