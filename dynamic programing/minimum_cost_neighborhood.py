def minimum_cost_dp(houses):
    dp = [(houses[0][0],houses[0][1], houses[0][2])]
    for i in range(1,len(houses)):
        dp_i_0 = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
        dp_i_1 = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
        dp_i_2 = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]
        dp.append((dp_i_0, dp_i_1, dp_i_2))
    return min(dp[-1][0], dp[-1][1], dp[-1][2])