def f(vals, wts, maxW):
    # dp=[|---max_weights->----]
    #    [|--------------------]
    #    [vals-----------------]
    dp = [[0 for _ in range(maxW + 1)] for _ in range(len(vals) + 1)] 

    for i in range(len(vals) + 1):
        for w in range(maxW + 1): 
            if i == 0 or w == 0: dp[i][w] = 0
            elif wts[i-1] <= w: dp[i][w] = max(vals[i-1] + dp[i-1][w-wts[i-1]], dp[i-1][w]) 
            else: dp[i][w] = dp[i-1][w] 
  
    return dp[-1][maxW]

print(f([60, 100, 120], [10, 20, 30], 50))
