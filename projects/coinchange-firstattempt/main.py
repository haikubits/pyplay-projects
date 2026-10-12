# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        d_mat = [0 for i in range(amount+1)]
        smallest_denomination = min(coins)
        for i in range(amount+1):
            if i == 0:
                d_mat[i] = 0
            elif i < smallest_denomination:
                d_mat[i] = -1
            else:
                min_coins = float("inf")
                for coin in coins:
                    if i < coin or d_mat[i - coin] == -1:
                        continue
                    else:
                        min_coins_needed = 1 + d_mat[i - coin]
                    if min_coins_needed < min_coins:
                        min_coins = min_coins_needed
                if not min_coins == float("inf"):
                    d_mat[i] = min_coins
                else:
                    d_mat[i] = -1
        return d_mat[amount]