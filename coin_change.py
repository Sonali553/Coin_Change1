def coin_change(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(0, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
print(coin_change([1, 4, 5], 11))
print(coin_change([2], 0))
print(coin_change([2], 3))
