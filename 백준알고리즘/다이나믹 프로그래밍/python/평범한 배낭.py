import sys
input = sys.stdin.readline

# N: 물건 개수 K:가방에 담을 수 있는 최대 무게
N, K = map(int, input().split())
# 각 물건의 무게와 가치
items = [list(map(int, input().split())) for _ in range(N)] 

def knapsack(N,K,items):
    dp = [[0]*(K+1) for _ in range(N+1)]

    # 가방에 담을 수 있는 물건의 개수를 1개부터 하나씩 늘려 나간다
    for i in range(1,N+1): # i: item
        weight, value = map(int, items[i-1])
        # 가방에 담을 수 있는 최대 무게를 1부터 차례대로 증가시켜 나가면서
        for j in range(1,K+1): # j:가방에 담을 수 있는 무게
            # 현재 물건이 가방이 담을 수 있는 무게보다 작으면
            print(weight, j, j - weight)
            if weight <= j:
                # 현재 물건을 넣지 않았을 때와 현재 물건을 넣었을 때의 가치를 비교한다.
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
            # 크면 이 물건을 담지 않고 이전 물건까지 담았을 때 가방에 담을 수 있는 최고 가치를 저장
            else:
                dp[i][j] = dp[i-1][j]

    # 가방에 담을 수 있는 최대 무게에서 모든 물건을 고려했을 때의 최대값을 출력
    return dp[N][K]


# 주어진 조건으로 가방싸기!
print(knapsack(N,K,items))








